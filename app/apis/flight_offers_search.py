import datetime
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from app.core.client import amadeus, ResponseError
from app.apis.auth_routes import get_current_user

router = APIRouter(prefix="/flight-offers-search", tags=["Flight Offers Search"])

# Airline Destinations Router
airline_router = APIRouter(prefix="/airline", tags=["Airline Destinations"])

class DepartureDateTimeRange(BaseModel):
    date: str
    time: str = "00:00:00"

class OriginDestination(BaseModel):
    id: str
    originLocationCode: str
    destinationLocationCode: str
    departureDateTimeRange: DepartureDateTimeRange

class Traveler(BaseModel):
    id: str
    travelerType: str  # ADULT, CHILD, HELD_INFANT, INFANT
    associatedAdultId: Optional[str] = None

class AdditionalInformation(BaseModel):
    chargeableCheckedBags: Optional[bool] = False
    brandedFares: Optional[bool] = False
    fareRules: Optional[bool] = False

class PricingOptions(BaseModel):
    includedCheckedBagsOnly: Optional[bool] = False

class CarrierRestrictions(BaseModel):
    blacklistedInEUAllowed: Optional[bool] = False
    includedCarrierCodes: Optional[List[str]] = None

class CabinRestriction(BaseModel):
    cabin: str  # ECONOMY, PREMIUM_ECONOMY, BUSINESS, FIRST
    coverage: str  # MOST_SEGMENTS, ALL_SEGMENTS
    originDestinationIds: List[str]

class ConnectionRestriction(BaseModel):
    airportChangeAllowed: Optional[bool] = False
    technicalStopsAllowed: Optional[bool] = False

class FlightFilters(BaseModel):
    crossBorderAllowed: Optional[bool] = True
    moreOvernightsAllowed: Optional[bool] = True
    returnToDepartureAirport: Optional[bool] = True
    railSegmentAllowed: Optional[bool] = True
    busSegmentAllowed: Optional[bool] = True
    carrierRestrictions: Optional[CarrierRestrictions] = None
    cabinRestrictions: Optional[List[CabinRestriction]] = None
    connectionRestriction: Optional[ConnectionRestriction] = None

class SearchCriteria(BaseModel):
    excludeAllotments: Optional[bool] = True
    addOneWayOffers: Optional[bool] = False
    maxFlightOffers: Optional[int] = 10
    allowAlternativeFareOptions: Optional[bool] = True
    oneFlightOfferPerDay: Optional[bool] = True
    additionalInformation: Optional[AdditionalInformation] = None
    pricingOptions: Optional[PricingOptions] = None
    flightFilters: Optional[FlightFilters] = None

class FlightSearchRequest(BaseModel):
    currencyCode: Optional[str] = None
    originDestinations: List[OriginDestination]
    travelers: List[Traveler]
    sources: Optional[List[str]] = ["GDS"]
    searchCriteria: Optional[SearchCriteria] = None

class FlightOfferSearch(BaseModel):
    origin_location_code: str
    destination_location_code: str
    departure_date: datetime.date
    return_date: Optional[datetime.date] = None
    adults: Optional[int] = 1
    included_airline_codes: Optional[List[str]] = None
    max: Optional[int] = 5
    # children: Optional[int] = None
    # infants: Optional[int] = None
    # currencyCode: Optional[str] = None
    # originDestinations: List[OriginDestination]
    # travelers: List[Traveler]
    # sources: Optional[List[str]] = ["GDS"]
    # searchCriteria: Optional[SearchCriteria] = None


class FlightOfferPricingRequest(BaseModel):
    flightOfferData: Dict[str, Any]


class FlightCreateOrderRequest(BaseModel):
    orderData: Dict[str, Any]

@router.get("/")
async def get_flight_offers(
    origin_location_code: str,
    destination_location_code: str,
    departure_date: str,
    return_date: Optional[str] = None,
    adults: int = 1,
    children: Optional[int] = None,
    included_airline_codes: Optional[str] = None,
    max: int = 5,
    current_user_id: int = Depends(get_current_user)
):
    """
    Get flight offers using the Amadeus API with GET parameters.
    
    Query Parameters:
    - origin_location_code: Airport/city code for departure (e.g., 'BOM')
    - destination_location_code: Airport/city code for arrival (e.g., 'BLR')
    - departure_date: Departure date (YYYY-MM-DD format, e.g., '2025-11-16')
    - return_date: Return date for round trips (optional, YYYY-MM-DD format)
    - adults: Number of adults (default: 1)
    - children: Number of children (optional)
    - included_airline_codes: Comma-separated airline codes (optional, e.g., 'AI,6E')
    - max: Maximum number of results (default: 5)
    """
    try:
        # Parse airline codes if provided
        airline_codes = None
        if included_airline_codes:
            airline_codes = included_airline_codes.split(',')
        
        # Build parameters for the API call
        params = {
            "originLocationCode": origin_location_code,
            "destinationLocationCode": destination_location_code,
            "departureDate": departure_date,
            "adults": adults,
            "max": max
        }
        
        # Add optional parameters
        if return_date:
            params["returnDate"] = return_date
        if children:
            params["children"] = children
        if airline_codes:
            params["includedAirlineCodes"] = airline_codes
        
        response = amadeus.shopping.flight_offers_search.get(**params)
        
        return {
            "success": True,
            "data": response.data,
            "meta": response.meta if hasattr(response, 'meta') else None
        }
        
    except ResponseError as error:
        raise HTTPException(
            status_code=error.status_code if hasattr(error, 'status_code') else 400,
            detail=str(error)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

@router.post("/pricing")
async def flight_offers_pricing(
    request: FlightOfferPricingRequest,
    current_user_id: int = Depends(get_current_user)
):
    try:
        response = amadeus.shopping.flight_offers.pricing.post(request.flightOfferData)

        return {
            "success": True,
            "data": response.data,
            "meta": response.meta if hasattr(response, "meta") else None,
        }

    except ResponseError as error:
        raise HTTPException(
            status_code=error.status_code if hasattr(error, "status_code") else 400,
            detail=str(error),
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}",
        )


@router.post("/orders")
async def create_flight_order(
    request: FlightCreateOrderRequest,
    current_user_id: int = Depends(get_current_user)
):
    try:
        import json
        # The frontend sends: {"orderData": {"data": {...}}}
        # So request.orderData is {"data": {...}}
        # The Amadeus SDK expects: {"data": {"type": "flight-order", "flightOffers": [...], "travelers": [...], ...}}
        order_data = request.orderData
        
        print("=== BOOKING REQUEST ===")
        print("Order data received:", json.dumps(order_data, indent=2)[:2000])
        
        # Validate that we have the correct structure
        if 'data' not in order_data:
            raise HTTPException(
                status_code=400,
                detail="Missing 'data' key in orderData"
            )
        
        inner_data = order_data['data']
        
        # Validate flight offer structure - the flightOfferPriceData should have all required fields
        if 'flightOffers' not in inner_data or len(inner_data['flightOffers']) == 0:
            raise HTTPException(
                status_code=400,
                detail="Missing or empty flightOffers array"
            )
        
        flight_offers = inner_data['flightOffers']
        first_offer = flight_offers[0]
        
        # Validate required fields in flightOfferPriceData
        required_fields = ['type', 'id', 'source', 'validatingAirlineCodes', 'itineraries', 'travelerPricings']
        missing_fields = [field for field in required_fields if field not in first_offer or not first_offer[field]]
        
        if missing_fields:
            print(f"WARNING: Missing fields in flightOfferPriceData: {missing_fields}")
            print("Flight offer keys:", list(first_offer.keys()) if isinstance(first_offer, dict) else "Not a dict")
        
        print("Flight offer validation:")
        print("  - Has type:", 'type' in first_offer if isinstance(first_offer, dict) else False, f"({first_offer.get('type', 'N/A')})")
        print("  - Has id:", 'id' in first_offer if isinstance(first_offer, dict) else False, f"({first_offer.get('id', 'N/A')})")
        print("  - Has source:", 'source' in first_offer if isinstance(first_offer, dict) else False, f"({first_offer.get('source', 'N/A')})")
        print("  - Has validatingAirlineCodes:", 'validatingAirlineCodes' in first_offer if isinstance(first_offer, dict) else False)
        print("  - Has itineraries:", 'itineraries' in first_offer if isinstance(first_offer, dict) else False)
        print("  - Has travelerPricings:", 'travelerPricings' in first_offer if isinstance(first_offer, dict) else False)
        
        # According to Amadeus API documentation:
        # https://developers.amadeus.com/self-service/category/flights/api-doc/flight-create-orders/api-reference
        # The request body should be: {"data": {"type": "flight-order", "flightOffers": [...], "travelers": [...], ...}}
        # order_data is already {"data": {...}}, so pass it directly
        # The travelers are already inside order_data['data']['travelers'], so no need to pass separately
        
        print("Request body being sent to Amadeus (first 2000 chars):", json.dumps(order_data, indent=2)[:2000])
        
        # The Amadeus SDK's post method expects the full request body
        # According to the official API docs, the body is {"data": {...}}
        # Pass order_data directly which matches this format
        response = amadeus.booking.flight_orders.post(order_data)

        return {
            "success": True,
            "data": response.data,
            "meta": response.meta if hasattr(response, "meta") else None,
        }

    except ResponseError as error:
        error_detail: Any = str(error)
        try:
            if hasattr(error, "response") and hasattr(error.response, "body"):
                import json  # type: ignore

                error_detail = json.loads(error.response.body)
        except Exception:
            error_detail = str(error)

        raise HTTPException(
            status_code=error.status_code if hasattr(error, "status_code") else 400,
            detail=error_detail,
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}",
        )

# @router.post("/")
# async def search_flight_offers(search_request: FlightSearchRequest):
#     """
#     Search for flight offers using the Amadeus API.
    
#     This endpoint uses the official Amadeus Flight Offers Search API with POST method.
    
#     Example Request:
#     ```json
#     {
#       "currencyCode": "USD",
#       "originDestinations": [
#         {
#           "id": "1",
#           "originLocationCode": "JFK",
#           "destinationLocationCode": "LAX",
#           "departureDateTimeRange": {
#             "date": "2024-12-15",
#             "time": "10:00:00"
#           }
#         },
#         {
#           "id": "2", 
#           "originLocationCode": "LAX",
#           "destinationLocationCode": "JFK",
#           "departureDateTimeRange": {
#             "date": "2024-12-22",
#             "time": "18:00:00"
#           }
#         }
#       ],
#       "travelers": [
#         {
#           "id": "1",
#           "travelerType": "ADULT"
#         },
#         {
#           "id": "2", 
#           "travelerType": "ADULT"
#         }
#       ],
#       "sources": ["GDS"],
#       "searchCriteria": {
#         "excludeAllotments": true,
#         "addOneWayOffers": false,
#         "maxFlightOffers": 20,
#         "allowAlternativeFareOptions": true,
#         "oneFlightOfferPerDay": false,
#         "additionalInformation": {
#           "chargeableCheckedBags": true,
#           "brandedFares": true,
#           "fareRules": false
#         },
#         "pricingOptions": {
#           "includedCheckedBagsOnly": false
#         },
#         "flightFilters": {
#           "crossBorderAllowed": true,
#           "moreOvernightsAllowed": true,
#           "returnToDepartureAirport": true,
#           "railSegmentAllowed": false,
#           "busSegmentAllowed": false,
#           "carrierRestrictions": {
#             "blacklistedInEUAllowed": false,
#             "includedCarrierCodes": ["AA", "DL", "UA"]
#           },
#           "cabinRestrictions": [
#             {
#               "cabin": "ECONOMY",
#               "coverage": "MOST_SEGMENTS",
#               "originDestinationIds": ["1", "2"]
#             }
#           ],
#           "connectionRestriction": {
#             "airportChangeAllowed": true,
#             "technicalStopsAllowed": false
#           }
#         }
#       }
#     }
#     ```
    
#     Parameters:
#     - currencyCode: Currency code for prices (e.g., 'USD', 'EUR', 'ZAR')
#     - originDestinations: List of origin-destination pairs with departure dates
#     - travelers: List of travelers with their types (ADULT, CHILD, HELD_INFANT, INFANT)
#     - sources: List of sources (default: ["GDS"])
#     - searchCriteria: Search filters and options
#     """
#     try:
#         # Convert Pydantic model to dict for API call
#         body = search_request.model_dump(exclude_unset=True)
        
#         # Make the API call using POST method
#         response = amadeus.shopping.flight_offers_search.post(body)
        
#         return {
#             "success": True,
#             "data": response.data,
#             "meta": response.meta if hasattr(response, 'meta') else None
#         }
        
#     except ResponseError as error:
#         raise HTTPException(
#             status_code=error.status_code if hasattr(error, 'status_code') else 400,
#             detail=str(error)
#         )
#     except Exception as e:
#         raise HTTPException(
#             status_code=500,
#             detail=f"Internal server error: {str(e)}"
#         )

# @router.get("/example")
# async def get_example_search():
    """
    Get an example flight search result to test the API using the official format.
    """
    try:
        # Example request body matching the official API format
        body = {
            "currencyCode": "ZAR",
            "originDestinations": [
                {
                    "id": "1",
                    "originLocationCode": "JNB",
                    "destinationLocationCode": "CPT",
                    "departureDateTimeRange": {
                        "date": "2022-07-01",
                        "time": "00:00:00"
                    }
                },
                {
                    "id": "2",
                    "originLocationCode": "CPT",
                    "destinationLocationCode": "JNB",
                    "departureDateTimeRange": {
                        "date": "2022-07-29",
                        "time": "00:00:00"
                    }
                }
            ],
            "travelers": [
                {
                    "id": "1",
                    "travelerType": "ADULT"
                },
                {
                    "id": "2",
                    "travelerType": "ADULT"
                },
                {
                    "id": "3",
                    "travelerType": "HELD_INFANT",
                    "associatedAdultId": "1"
                }
            ],
            "sources": ["GDS"],
            "searchCriteria": {
                "excludeAllotments": True,
                "addOneWayOffers": False,
                "maxFlightOffers": 10,
                "allowAlternativeFareOptions": True,
                "oneFlightOfferPerDay": True,
                "additionalInformation": {
                    "chargeableCheckedBags": True,
                    "brandedFares": True,
                    "fareRules": False
                },
                "pricingOptions": {
                    "includedCheckedBagsOnly": False
                },
                "flightFilters": {
                    "crossBorderAllowed": True,
                    "moreOvernightsAllowed": True,
                    "returnToDepartureAirport": True,
                    "railSegmentAllowed": True,
                    "busSegmentAllowed": True,
                    "carrierRestrictions": {
                        "blacklistedInEUAllowed": True,
                        "includedCarrierCodes": ["FA"]
                    },
                    "cabinRestrictions": [
                        {
                            "cabin": "ECONOMY",
                            "coverage": "MOST_SEGMENTS",
                            "originDestinationIds": ["2"]
                        },
                        {
                            "cabin": "ECONOMY",
                            "coverage": "MOST_SEGMENTS",
                            "originDestinationIds": ["1"]
                        }
                    ],
                    "connectionRestriction": {
                        "airportChangeAllowed": True,
                        "technicalStopsAllowed": True
                    }
                }
            }
        }
        
        response = amadeus.shopping.flight_offers_search.post(body)
        
        return {
            "success": True,
            "data": response.data,
            "meta": response.meta if hasattr(response, 'meta') else None
        }
        
    except ResponseError as error:
        raise HTTPException(
            status_code=error.status_code if hasattr(error, 'status_code') else 400,
            detail=str(error)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

# Airline Destinations Endpoints
@airline_router.get("/destinations/{airline_code}")
async def get_airline_destinations(
    airline_code: str,
    current_user_id: int = Depends(get_current_user)
):
    """
    Get all destinations served by a specific airline.
    
    Example:
    GET /airline/destinations/BA
    
    This will return all destinations served by British Airways (BA).
    
    Parameters:
    - airline_code: IATA airline code (e.g., 'BA', 'AA', 'DL')
    """
    try:
        response = amadeus.airline.destinations.get(airlineCode=airline_code)
        
        return {
            "success": True,
            "data": response.data,
            "meta": response.meta if hasattr(response, 'meta') else None
        }
        
    except ResponseError as error:
        raise HTTPException(
            status_code=error.status_code if hasattr(error, 'status_code') else 400,
            detail=str(error)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )
