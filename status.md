# Retesting Issue

## Step-1:

Flight Search Response: Success

```json
{
  "success": true,
  "data": [
    {
      "type": "flight-offer",
      "id": "1",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "isUpsellOffer": false,
      "lastTicketingDate": "2025-11-16",
      "lastTicketingDateTime": "2025-11-16",
      "numberOfBookableSeats": 6,
      "itineraries": [
        {
          "duration": "PT1H55M",
          "segments": [
            {
              "departure": {
                "iataCode": "BOM",
                "terminal": "2",
                "at": "2025-11-18T15:20:00"
              },
              "arrival": {
                "iataCode": "BLR",
                "terminal": "2",
                "at": "2025-11-18T17:15:00"
              },
              "carrierCode": "AI",
              "number": "2853",
              "aircraft": { "code": "32N" },
              "operating": { "carrierCode": "AI" },
              "duration": "PT1H55M",
              "id": "6",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        }
      ],
      "price": {
        "currency": "EUR",
        "total": "62.75",
        "base": "54.00",
        "fees": [
          { "amount": "0.00", "type": "SUPPLIER" },
          { "amount": "0.00", "type": "TICKETING" }
        ],
        "grandTotal": "62.75"
      },
      "pricingOptions": {
        "fareType": ["PUBLISHED"],
        "includedCheckedBagsOnly": true
      },
      "validatingAirlineCodes": ["AI"],
      "travelerPricings": [
        {
          "travelerId": "1",
          "fareOption": "STANDARD",
          "travelerType": "ADULT",
          "price": { "currency": "EUR", "total": "62.75", "base": "54.00" },
          "fareDetailsBySegment": [
            {
              "segmentId": "6",
              "cabin": "ECONOMY",
              "fareBasis": "GU1YXSII",
              "brandedFare": "ECOVALU",
              "brandedFareLabel": "ECO VALUE",
              "class": "G",
              "includedCheckedBags": { "weight": 15, "weightUnit": "KG" },
              "includedCabinBags": { "weight": 7, "weightUnit": "KG" },
              "amenities": [
                {
                  "description": "PRE RESERVED SEAT ASSIGNMENT",
                  "isChargeable": false,
                  "amenityType": "PRE_RESERVED_SEAT",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "MEAL SERVICES",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "REFUNDABLE TICKET",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "CHANGEABLE TICKET",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "UPGRADE",
                  "isChargeable": true,
                  "amenityType": "UPGRADES",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "FREE CHECKED BAGGAGE ALLOWANCE",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": { "name": "BrandedFare" }
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "flight-offer",
      "id": "2",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "isUpsellOffer": false,
      "lastTicketingDate": "2025-11-16",
      "lastTicketingDateTime": "2025-11-16",
      "numberOfBookableSeats": 9,
      "itineraries": [
        {
          "duration": "PT4H50M",
          "segments": [
            {
              "departure": {
                "iataCode": "BOM",
                "terminal": "2",
                "at": "2025-11-18T15:30:00"
              },
              "arrival": { "iataCode": "GOI", "at": "2025-11-18T16:50:00" },
              "carrierCode": "AI",
              "number": "2745",
              "aircraft": { "code": "32N" },
              "operating": { "carrierCode": "AI" },
              "duration": "PT1H20M",
              "id": "3",
              "numberOfStops": 0,
              "blacklistedInEU": false
            },
            {
              "departure": { "iataCode": "GOI", "at": "2025-11-18T19:00:00" },
              "arrival": {
                "iataCode": "BLR",
                "terminal": "2",
                "at": "2025-11-18T20:20:00"
              },
              "carrierCode": "AI",
              "number": "9529",
              "aircraft": { "code": "320" },
              "operating": { "carrierCode": "IX" },
              "duration": "PT1H20M",
              "id": "4",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        }
      ],
      "price": {
        "currency": "EUR",
        "total": "64.49",
        "base": "54.00",
        "fees": [
          { "amount": "0.00", "type": "SUPPLIER" },
          { "amount": "0.00", "type": "TICKETING" }
        ],
        "grandTotal": "64.49"
      },
      "pricingOptions": {
        "fareType": ["PUBLISHED"],
        "includedCheckedBagsOnly": true
      },
      "validatingAirlineCodes": ["AI"],
      "travelerPricings": [
        {
          "travelerId": "1",
          "fareOption": "STANDARD",
          "travelerType": "ADULT",
          "price": { "currency": "EUR", "total": "64.49", "base": "54.00" },
          "fareDetailsBySegment": [
            {
              "segmentId": "3",
              "cabin": "ECONOMY",
              "fareBasis": "SU1YXRII",
              "brandedFare": "ECOVALU",
              "brandedFareLabel": "ECO VALUE",
              "class": "S",
              "includedCheckedBags": { "weight": 15, "weightUnit": "KG" },
              "includedCabinBags": { "weight": 7, "weightUnit": "KG" },
              "amenities": [
                {
                  "description": "PRE RESERVED SEAT ASSIGNMENT",
                  "isChargeable": false,
                  "amenityType": "PRE_RESERVED_SEAT",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "MEAL SERVICES",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "REFUNDABLE TICKET",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "CHANGEABLE TICKET",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "UPGRADE",
                  "isChargeable": true,
                  "amenityType": "UPGRADES",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "FREE CHECKED BAGGAGE ALLOWANCE",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": { "name": "BrandedFare" }
                }
              ]
            },
            {
              "segmentId": "4",
              "cabin": "ECONOMY",
              "fareBasis": "SL1YXYII",
              "brandedFare": "ECOVALU",
              "brandedFareLabel": "ECO VALUE",
              "class": "S",
              "includedCheckedBags": { "weight": 15, "weightUnit": "KG" },
              "amenities": [
                {
                  "description": "PRE RESERVED SEAT ASSIGNMENT",
                  "isChargeable": false,
                  "amenityType": "PRE_RESERVED_SEAT",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "MEAL SERVICES",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "REFUNDABLE TICKET",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "CHANGEABLE TICKET",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "UPGRADE",
                  "isChargeable": true,
                  "amenityType": "UPGRADES",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "FREE CHECKED BAGGAGE ALLOWANCE",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": { "name": "BrandedFare" }
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "flight-offer",
      "id": "3",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "isUpsellOffer": false,
      "lastTicketingDate": "2025-11-16",
      "lastTicketingDateTime": "2025-11-16",
      "numberOfBookableSeats": 9,
      "itineraries": [
        {
          "duration": "PT1H45M",
          "segments": [
            {
              "departure": {
                "iataCode": "BOM",
                "terminal": "2",
                "at": "2025-11-18T06:00:00"
              },
              "arrival": {
                "iataCode": "BLR",
                "terminal": "2",
                "at": "2025-11-18T07:45:00"
              },
              "carrierCode": "AI",
              "number": "2845",
              "aircraft": { "code": "321" },
              "operating": { "carrierCode": "AI" },
              "duration": "PT1H45M",
              "id": "2",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        }
      ],
      "price": {
        "currency": "EUR",
        "total": "68.00",
        "base": "59.00",
        "fees": [
          { "amount": "0.00", "type": "SUPPLIER" },
          { "amount": "0.00", "type": "TICKETING" }
        ],
        "grandTotal": "68.00"
      },
      "pricingOptions": {
        "fareType": ["PUBLISHED"],
        "includedCheckedBagsOnly": true
      },
      "validatingAirlineCodes": ["AI"],
      "travelerPricings": [
        {
          "travelerId": "1",
          "fareOption": "STANDARD",
          "travelerType": "ADULT",
          "price": { "currency": "EUR", "total": "68.00", "base": "59.00" },
          "fareDetailsBySegment": [
            {
              "segmentId": "2",
              "cabin": "ECONOMY",
              "fareBasis": "WU1YXSII",
              "brandedFare": "ECOVALU",
              "brandedFareLabel": "ECO VALUE",
              "class": "W",
              "includedCheckedBags": { "weight": 15, "weightUnit": "KG" },
              "includedCabinBags": { "weight": 7, "weightUnit": "KG" },
              "amenities": [
                {
                  "description": "PRE RESERVED SEAT ASSIGNMENT",
                  "isChargeable": false,
                  "amenityType": "PRE_RESERVED_SEAT",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "MEAL SERVICES",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "REFUNDABLE TICKET",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "CHANGEABLE TICKET",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "UPGRADE",
                  "isChargeable": true,
                  "amenityType": "UPGRADES",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "FREE CHECKED BAGGAGE ALLOWANCE",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": { "name": "BrandedFare" }
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "flight-offer",
      "id": "4",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "isUpsellOffer": false,
      "lastTicketingDate": "2025-11-16",
      "lastTicketingDateTime": "2025-11-16",
      "numberOfBookableSeats": 9,
      "itineraries": [
        {
          "duration": "PT1H55M",
          "segments": [
            {
              "departure": {
                "iataCode": "BOM",
                "terminal": "2",
                "at": "2025-11-18T06:35:00"
              },
              "arrival": {
                "iataCode": "BLR",
                "terminal": "2",
                "at": "2025-11-18T08:30:00"
              },
              "carrierCode": "AI",
              "number": "2603",
              "aircraft": { "code": "32N" },
              "operating": { "carrierCode": "AI" },
              "duration": "PT1H55M",
              "id": "5",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        }
      ],
      "price": {
        "currency": "EUR",
        "total": "68.00",
        "base": "59.00",
        "fees": [
          { "amount": "0.00", "type": "SUPPLIER" },
          { "amount": "0.00", "type": "TICKETING" }
        ],
        "grandTotal": "68.00"
      },
      "pricingOptions": {
        "fareType": ["PUBLISHED"],
        "includedCheckedBagsOnly": true
      },
      "validatingAirlineCodes": ["AI"],
      "travelerPricings": [
        {
          "travelerId": "1",
          "fareOption": "STANDARD",
          "travelerType": "ADULT",
          "price": { "currency": "EUR", "total": "68.00", "base": "59.00" },
          "fareDetailsBySegment": [
            {
              "segmentId": "5",
              "cabin": "ECONOMY",
              "fareBasis": "WU1YXSII",
              "brandedFare": "ECOVALU",
              "brandedFareLabel": "ECO VALUE",
              "class": "W",
              "includedCheckedBags": { "weight": 15, "weightUnit": "KG" },
              "includedCabinBags": { "weight": 7, "weightUnit": "KG" },
              "amenities": [
                {
                  "description": "PRE RESERVED SEAT ASSIGNMENT",
                  "isChargeable": false,
                  "amenityType": "PRE_RESERVED_SEAT",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "MEAL SERVICES",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "REFUNDABLE TICKET",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "CHANGEABLE TICKET",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "UPGRADE",
                  "isChargeable": true,
                  "amenityType": "UPGRADES",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "FREE CHECKED BAGGAGE ALLOWANCE",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": { "name": "BrandedFare" }
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "flight-offer",
      "id": "5",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "isUpsellOffer": false,
      "lastTicketingDate": "2025-11-16",
      "lastTicketingDateTime": "2025-11-16",
      "numberOfBookableSeats": 9,
      "itineraries": [
        {
          "duration": "PT2H10M",
          "segments": [
            {
              "departure": {
                "iataCode": "BOM",
                "terminal": "2",
                "at": "2025-11-18T02:55:00"
              },
              "arrival": {
                "iataCode": "BLR",
                "terminal": "2",
                "at": "2025-11-18T05:05:00"
              },
              "carrierCode": "AI",
              "number": "2812",
              "aircraft": { "code": "32N" },
              "operating": { "carrierCode": "AI" },
              "duration": "PT2H10M",
              "id": "1",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        }
      ],
      "price": {
        "currency": "EUR",
        "total": "68.00",
        "base": "59.00",
        "fees": [
          { "amount": "0.00", "type": "SUPPLIER" },
          { "amount": "0.00", "type": "TICKETING" }
        ],
        "grandTotal": "68.00"
      },
      "pricingOptions": {
        "fareType": ["PUBLISHED"],
        "includedCheckedBagsOnly": true
      },
      "validatingAirlineCodes": ["AI"],
      "travelerPricings": [
        {
          "travelerId": "1",
          "fareOption": "STANDARD",
          "travelerType": "ADULT",
          "price": { "currency": "EUR", "total": "68.00", "base": "59.00" },
          "fareDetailsBySegment": [
            {
              "segmentId": "1",
              "cabin": "ECONOMY",
              "fareBasis": "WU1YXSII",
              "brandedFare": "ECOVALU",
              "brandedFareLabel": "ECO VALUE",
              "class": "W",
              "includedCheckedBags": { "weight": 15, "weightUnit": "KG" },
              "includedCabinBags": { "weight": 7, "weightUnit": "KG" },
              "amenities": [
                {
                  "description": "PRE RESERVED SEAT ASSIGNMENT",
                  "isChargeable": false,
                  "amenityType": "PRE_RESERVED_SEAT",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "MEAL SERVICES",
                  "isChargeable": false,
                  "amenityType": "MEAL",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "REFUNDABLE TICKET",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "CHANGEABLE TICKET",
                  "isChargeable": true,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "UPGRADE",
                  "isChargeable": true,
                  "amenityType": "UPGRADES",
                  "amenityProvider": { "name": "BrandedFare" }
                },
                {
                  "description": "FREE CHECKED BAGGAGE ALLOWANCE",
                  "isChargeable": false,
                  "amenityType": "BRANDED_FARES",
                  "amenityProvider": { "name": "BrandedFare" }
                }
              ]
            }
          ]
        }
      ]
    }
  ],
  "meta": null
}
```

## Step-2: Detailed pricing response

Status: Success

```json
{
  "success": true,
  "data": {
    "type": "flight-offers-pricing",
    "flightOffers": [
      {
        "type": "flight-offer",
        "id": "1",
        "source": "GDS",
        "instantTicketingRequired": false,
        "nonHomogeneous": false,
        "paymentCardRequired": false,
        "lastTicketingDate": "2025-11-16",
        "itineraries": [
          {
            "segments": [
              {
                "departure": {
                  "iataCode": "BOM",
                  "terminal": "2",
                  "at": "2025-11-18T15:20:00"
                },
                "arrival": {
                  "iataCode": "BLR",
                  "terminal": "2",
                  "at": "2025-11-18T17:15:00"
                },
                "carrierCode": "AI",
                "number": "2853",
                "aircraft": { "code": "32N" },
                "operating": { "carrierCode": "AI" },
                "duration": "PT1H55M",
                "id": "6",
                "numberOfStops": 0,
                "co2Emissions": [
                  { "weight": 60, "weightUnit": "KG", "cabin": "ECONOMY" }
                ]
              }
            ]
          }
        ],
        "price": {
          "currency": "EUR",
          "total": "62.75",
          "base": "54.00",
          "fees": [
            { "amount": "0.00", "type": "SUPPLIER" },
            { "amount": "0.00", "type": "TICKETING" },
            { "amount": "0.00", "type": "FORM_OF_PAYMENT" }
          ],
          "grandTotal": "62.75",
          "billingCurrency": "EUR"
        },
        "pricingOptions": {
          "fareType": ["PUBLISHED"],
          "includedCheckedBagsOnly": true
        },
        "validatingAirlineCodes": ["AI"],
        "travelerPricings": [
          {
            "travelerId": "1",
            "fareOption": "STANDARD",
            "travelerType": "ADULT",
            "price": {
              "currency": "EUR",
              "total": "62.75",
              "base": "54.00",
              "taxes": [
                { "amount": "2.29", "code": "P2" },
                { "amount": "2.01", "code": "IN" },
                { "amount": "2.79", "code": "K3" },
                { "amount": "1.66", "code": "YR" }
              ],
              "refundableTaxes": "12.75"
            },
            "fareDetailsBySegment": [
              {
                "segmentId": "6",
                "cabin": "ECONOMY",
                "fareBasis": "GU1YXSII",
                "brandedFare": "ECOVALU",
                "class": "G",
                "includedCheckedBags": { "weight": 15, "weightUnit": "KG" }
              }
            ]
          }
        ]
      }
    ],
    "bookingRequirements": {
      "emailAddressRequired": true,
      "mobilePhoneNumberRequired": true
    }
  },
  "meta": null
}
```

## Step-3: Book Flight

Request Json

```json
{
  "orderData": {
    "data": {
      "type": "flight-order",
      "flightOffers": [
        {
          "type": "flight-offer",
          "id": "1",
          "source": "GDS",
          "instantTicketingRequired": false,
          "nonHomogeneous": false,
          "paymentCardRequired": false,
          "lastTicketingDate": "2025-11-16",
          "itineraries": [
            {
              "segments": [
                {
                  "departure": {
                    "iataCode": "BOM",
                    "terminal": "2",
                    "at": "2025-11-18T15:20:00"
                  },
                  "arrival": {
                    "iataCode": "BLR",
                    "terminal": "2",
                    "at": "2025-11-18T17:15:00"
                  },
                  "carrierCode": "AI",
                  "number": "2853",
                  "aircraft": { "code": "32N" },
                  "operating": { "carrierCode": "AI" },
                  "duration": "PT1H55M",
                  "id": "6",
                  "numberOfStops": 0,
                  "co2Emissions": [
                    { "weight": 60, "weightUnit": "KG", "cabin": "ECONOMY" }
                  ]
                }
              ]
            }
          ],
          "price": {
            "currency": "EUR",
            "total": "62.75",
            "base": "54.00",
            "fees": [
              { "amount": "0.00", "type": "SUPPLIER" },
              { "amount": "0.00", "type": "TICKETING" },
              { "amount": "0.00", "type": "FORM_OF_PAYMENT" }
            ],
            "grandTotal": "62.75",
            "billingCurrency": "EUR"
          },
          "pricingOptions": {
            "fareType": ["PUBLISHED"],
            "includedCheckedBagsOnly": true
          },
          "validatingAirlineCodes": ["AI"],
          "travelerPricings": [
            {
              "travelerId": "1",
              "fareOption": "STANDARD",
              "travelerType": "ADULT",
              "price": {
                "currency": "EUR",
                "total": "62.75",
                "base": "54.00",
                "taxes": [
                  { "amount": "2.29", "code": "P2" },
                  { "amount": "2.01", "code": "IN" },
                  { "amount": "2.79", "code": "K3" },
                  { "amount": "1.66", "code": "YR" }
                ],
                "refundableTaxes": "12.75"
              },
              "fareDetailsBySegment": [
                {
                  "segmentId": "6",
                  "cabin": "ECONOMY",
                  "fareBasis": "GU1YXSII",
                  "brandedFare": "ECOVALU",
                  "class": "G",
                  "includedCheckedBags": { "weight": 15, "weightUnit": "KG" }
                }
              ]
            }
          ]
        }
      ],
      "travelers": [
        {
          "id": "1",
          "dateOfBirth": "1982-01-16",
          "name": { "firstName": "JORGE", "lastName": "GONZALES" },
          "gender": "MALE",
          "contact": {
            "emailAddress": "jorge.gonzales833@telefonica.es",
            "phones": [
              {
                "deviceType": "MOBILE",
                "countryCallingCode": "34",
                "number": "480080076"
              }
            ]
          },
          "documents": [
            {
              "documentType": "PASSPORT",
              "birthPlace": "Madrid",
              "issuanceLocation": "Madrid",
              "issuanceDate": "2015-04-14",
              "number": "00000000",
              "expiryDate": "2030-01-14",
              "issuanceCountry": "ES",
              "validityCountry": "ES",
              "nationality": "ES",
              "holder": true
            }
          ]
        }
      ],
      "remarks": {
        "general": [
          {
            "subType": "GENERAL_MISCELLANEOUS",
            "text": "ONLINE BOOKING FROM XPLRO"
          }
        ]
      },
      "ticketingAgreement": { "option": "DELAY_TO_CANCEL", "delay": "6D" },
      "contacts": [
        {
          "addresseeName": { "firstName": "Sanjay", "lastName": "Patel" },
          "companyName": "XPLRO",
          "purpose": "STANDARD",
          "phones": [
            {
              "deviceType": "MOBILE",
              "countryCallingCode": "1",
              "number": "1234567890"
            }
          ],
          "emailAddress": "cenzer2@gmail.com",
          "address": {
            "lines": ["123 Main St"],
            "postalCode": "12345",
            "cityName": "City",
            "countryCode": "US"
          }
        }
      ]
    }
  }
}
```

### Status: Error

error response

```json
{
  "orderData": {
    "data": {
      "type": "flight-order",
      "flightOffers": [
        {
          "type": "flight-offer",
          "id": "1",
          "source": "GDS",
          "instantTicketingRequired": false,
          "nonHomogeneous": false,
          "paymentCardRequired": false,
          "lastTicketingDate": "2025-11-16",
          "itineraries": [
            {
              "segments": [
                {
                  "departure": {
                    "iataCode": "BOM",
                    "terminal": "2",
                    "at": "2025-11-18T15:20:00"
                  },
                  "arrival": {
                    "iataCode": "BLR",
                    "terminal": "2",
                    "at": "2025-11-18T17:15:00"
                  },
                  "carrierCode": "AI",
                  "number": "2853",
                  "aircraft": { "code": "32N" },
                  "operating": { "carrierCode": "AI" },
                  "duration": "PT1H55M",
                  "id": "6",
                  "numberOfStops": 0,
                  "co2Emissions": [
                    { "weight": 60, "weightUnit": "KG", "cabin": "ECONOMY" }
                  ]
                }
              ]
            }
          ],
          "price": {
            "currency": "EUR",
            "total": "62.75",
            "base": "54.00",
            "fees": [
              { "amount": "0.00", "type": "SUPPLIER" },
              { "amount": "0.00", "type": "TICKETING" },
              { "amount": "0.00", "type": "FORM_OF_PAYMENT" }
            ],
            "grandTotal": "62.75",
            "billingCurrency": "EUR"
          },
          "pricingOptions": {
            "fareType": ["PUBLISHED"],
            "includedCheckedBagsOnly": true
          },
          "validatingAirlineCodes": ["AI"],
          "travelerPricings": [
            {
              "travelerId": "1",
              "fareOption": "STANDARD",
              "travelerType": "ADULT",
              "price": {
                "currency": "EUR",
                "total": "62.75",
                "base": "54.00",
                "taxes": [
                  { "amount": "2.29", "code": "P2" },
                  { "amount": "2.01", "code": "IN" },
                  { "amount": "2.79", "code": "K3" },
                  { "amount": "1.66", "code": "YR" }
                ],
                "refundableTaxes": "12.75"
              },
              "fareDetailsBySegment": [
                {
                  "segmentId": "6",
                  "cabin": "ECONOMY",
                  "fareBasis": "GU1YXSII",
                  "brandedFare": "ECOVALU",
                  "class": "G",
                  "includedCheckedBags": { "weight": 15, "weightUnit": "KG" }
                }
              ]
            }
          ]
        }
      ],
      "travelers": [
        {
          "id": "1",
          "dateOfBirth": "1982-01-16",
          "name": { "firstName": "JORGE", "lastName": "GONZALES" },
          "gender": "MALE",
          "contact": {
            "emailAddress": "jorge.gonzales833@telefonica.es",
            "phones": [
              {
                "deviceType": "MOBILE",
                "countryCallingCode": "34",
                "number": "480080076"
              }
            ]
          },
          "documents": [
            {
              "documentType": "PASSPORT",
              "birthPlace": "Madrid",
              "issuanceLocation": "Madrid",
              "issuanceDate": "2015-04-14",
              "number": "00000000",
              "expiryDate": "2030-01-14",
              "issuanceCountry": "ES",
              "validityCountry": "ES",
              "nationality": "ES",
              "holder": true
            }
          ]
        }
      ],
      "remarks": {
        "general": [
          {
            "subType": "GENERAL_MISCELLANEOUS",
            "text": "ONLINE BOOKING FROM XPLRO"
          }
        ]
      },
      "ticketingAgreement": { "option": "DELAY_TO_CANCEL", "delay": "6D" },
      "contacts": [
        {
          "addresseeName": { "firstName": "Sanjay", "lastName": "Patel" },
          "companyName": "XPLRO",
          "purpose": "STANDARD",
          "phones": [
            {
              "deviceType": "MOBILE",
              "countryCallingCode": "1",
              "number": "1234567890"
            }
          ],
          "emailAddress": "cenzer2@gmail.com",
          "address": {
            "lines": ["123 Main St"],
            "postalCode": "12345",
            "cityName": "City",
            "countryCode": "US"
          }
        }
      ]
    }
  }
}
```

## What does the Document says for the correct process

see each reqeust one by one in this

```json
# offer Search

{
    "meta": {
        "count": 1,
        "links": {
            "self": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=PAR&destinationLocationCode=ICN&departureDate=2025-11-30&returnDate=2025-12-14&adults=2&max=1"
        }
    },
    "data": [
        {
            "type": "flight-offer",
            "id": "1",
            "source": "GDS",
            "instantTicketingRequired": false,
            "nonHomogeneous": false,
            "oneWay": false,
            "isUpsellOffer": false,
            "lastTicketingDate": "2025-11-30",
            "lastTicketingDateTime": "2025-11-30",
            "numberOfBookableSeats": 9,
            "itineraries": [
                {
                    "duration": "PT32H55M",
                    "segments": [
                        {
                            "departure": {
                                "iataCode": "CDG",
                                "at": "2025-11-30T15:25:00"
                            },
                            "arrival": {
                                "iataCode": "HEL",
                                "at": "2025-11-30T19:20:00"
                            },
                            "carrierCode": "6X",
                            "number": "3618",
                            "aircraft": {
                                "code": "733"
                            },
                            "operating": {
                                "carrierCode": "6X"
                            },
                            "duration": "PT2H55M",
                            "id": "1",
                            "numberOfStops": 0,
                            "blacklistedInEU": false
                        },
                        {
                            "departure": {
                                "iataCode": "HEL",
                                "at": "2025-12-01T17:30:00"
                            },
                            "arrival": {
                                "iataCode": "ICN",
                                "at": "2025-12-02T08:20:00"
                            },
                            "carrierCode": "6X",
                            "number": "3605",
                            "aircraft": {
                                "code": "733"
                            },
                            "operating": {
                                "carrierCode": "6X"
                            },
                            "duration": "PT7H50M",
                            "id": "2",
                            "numberOfStops": 0,
                            "blacklistedInEU": false
                        }
                    ]
                },
                {
                    "duration": "PT11H17M",
                    "segments": [
                        {
                            "departure": {
                                "iataCode": "ICN",
                                "at": "2025-12-14T09:53:00"
                            },
                            "arrival": {
                                "iataCode": "CDG",
                                "at": "2025-12-14T14:10:00"
                            },
                            "carrierCode": "6X",
                            "number": "957",
                            "aircraft": {
                                "code": "332"
                            },
                            "operating": {
                                "carrierCode": "6X"
                            },
                            "duration": "PT11H17M",
                            "id": "3",
                            "numberOfStops": 0,
                            "blacklistedInEU": false
                        }
                    ]
                }
            ],
            "price": {
                "currency": "EUR",
                "total": "436.16",
                "base": "242.00",
                "fees": [
                    {
                        "amount": "0.00",
                        "type": "SUPPLIER"
                    },
                    {
                        "amount": "0.00",
                        "type": "TICKETING"
                    }
                ],
                "grandTotal": "436.16",
                "additionalServices": [
                    {
                        "amount": "3.00",
                        "type": "CHECKED_BAGS"
                    }
                ]
            },
            "pricingOptions": {
                "fareType": [
                    "PUBLISHED"
                ],
                "includedCheckedBagsOnly": true
            },
            "validatingAirlineCodes": [
                "6X"
            ],
            "travelerPricings": [
                {
                    "travelerId": "1",
                    "fareOption": "STANDARD",
                    "travelerType": "ADULT",
                    "price": {
                        "currency": "EUR",
                        "total": "218.08",
                        "base": "121.00"
                    },
                    "fareDetailsBySegment": [
                        {
                            "segmentId": "1",
                            "cabin": "ECONOMY",
                            "fareBasis": "YCNV1",
                            "class": "Y",
                            "includedCheckedBags": {
                                "quantity": 1
                            }
                        },
                        {
                            "segmentId": "2",
                            "cabin": "ECONOMY",
                            "fareBasis": "YCNV1",
                            "class": "Y",
                            "includedCheckedBags": {
                                "quantity": 1
                            }
                        },
                        {
                            "segmentId": "3",
                            "cabin": "ECONOMY",
                            "fareBasis": "YCNV1",
                            "class": "Y",
                            "includedCheckedBags": {
                                "quantity": 1
                            }
                        }
                    ]
                },
                {
                    "travelerId": "2",
                    "fareOption": "STANDARD",
                    "travelerType": "ADULT",
                    "price": {
                        "currency": "EUR",
                        "total": "218.08",
                        "base": "121.00"
                    },
                    "fareDetailsBySegment": [
                        {
                            "segmentId": "1",
                            "cabin": "ECONOMY",
                            "fareBasis": "YCNV1",
                            "class": "Y",
                            "includedCheckedBags": {
                                "quantity": 1
                            }
                        },
                        {
                            "segmentId": "2",
                            "cabin": "ECONOMY",
                            "fareBasis": "YCNV1",
                            "class": "Y",
                            "includedCheckedBags": {
                                "quantity": 1
                            }
                        },
                        {
                            "segmentId": "3",
                            "cabin": "ECONOMY",
                            "fareBasis": "YCNV1",
                            "class": "Y",
                            "includedCheckedBags": {
                                "quantity": 1
                            }
                        }
                    ]
                }
            ]
        }
    ],
    "dictionaries": {
        "locations": {
            "ICN": {
                "cityCode": "SEL",
                "countryCode": "KR"
            },
            "CDG": {
                "cityCode": "PAR",
                "countryCode": "FR"
            },
            "HEL": {
                "cityCode": "HEL",
                "countryCode": "FI"
            }
        },
        "aircraft": {
            "332": "AIRBUS A330-200",
            "733": "BOEING 737-300"
        },
        "currencies": {
            "EUR": "EURO"
        },
        "carriers": {
            "6X": "AMADEUS SIX"
        }
    }
}
===========

# offer pricing
{
    "data": {
        "type": "flight-offers-pricing",
        "flightOffers": [
            {
                "type": "flight-offer",
                "id": "1",
                "source": "GDS",
                "instantTicketingRequired": false,
                "nonHomogeneous": false,
                "paymentCardRequired": false,
                "lastTicketingDate": "2025-11-30",
                "itineraries": [
                    {
                        "segments": [
                            {
                                "departure": {
                                    "iataCode": "CDG",
                                    "at": "2025-11-30T15:25:00"
                                },
                                "arrival": {
                                    "iataCode": "HEL",
                                    "at": "2025-11-30T19:20:00"
                                },
                                "carrierCode": "6X",
                                "number": "3618",
                                "aircraft": {
                                    "code": "733"
                                },
                                "operating": {
                                    "carrierCode": "6X"
                                },
                                "duration": "PT2H55M",
                                "id": "1",
                                "numberOfStops": 0,
                                "co2Emissions": [
                                    {
                                        "weight": 175,
                                        "weightUnit": "KG",
                                        "cabin": "ECONOMY"
                                    }
                                ]
                            },
                            {
                                "departure": {
                                    "iataCode": "HEL",
                                    "at": "2025-12-01T17:30:00"
                                },
                                "arrival": {
                                    "iataCode": "ICN",
                                    "at": "2025-12-02T08:20:00"
                                },
                                "carrierCode": "6X",
                                "number": "3605",
                                "aircraft": {
                                    "code": "733"
                                },
                                "operating": {
                                    "carrierCode": "6X"
                                },
                                "duration": "PT7H50M",
                                "id": "2",
                                "numberOfStops": 0,
                                "co2Emissions": [
                                    {
                                        "weight": 295,
                                        "weightUnit": "KG",
                                        "cabin": "ECONOMY"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "segments": [
                            {
                                "departure": {
                                    "iataCode": "ICN",
                                    "at": "2025-12-14T09:53:00"
                                },
                                "arrival": {
                                    "iataCode": "CDG",
                                    "at": "2025-12-14T14:10:00"
                                },
                                "carrierCode": "6X",
                                "number": "957",
                                "aircraft": {
                                    "code": "332"
                                },
                                "operating": {
                                    "carrierCode": "6X"
                                },
                                "duration": "PT12H17M",
                                "id": "3",
                                "numberOfStops": 0,
                                "co2Emissions": [
                                    {
                                        "weight": 381,
                                        "weightUnit": "KG",
                                        "cabin": "ECONOMY"
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "price": {
                    "currency": "EUR",
                    "total": "436.16",
                    "base": "242.00",
                    "fees": [
                        {
                            "amount": "0.00",
                            "type": "SUPPLIER"
                        },
                        {
                            "amount": "0.00",
                            "type": "TICKETING"
                        },
                        {
                            "amount": "0.00",
                            "type": "FORM_OF_PAYMENT"
                        }
                    ],
                    "grandTotal": "436.16",
                    "billingCurrency": "EUR"
                },
                "pricingOptions": {
                    "fareType": [
                        "PUBLISHED"
                    ],
                    "includedCheckedBagsOnly": true
                },
                "validatingAirlineCodes": [
                    "6X"
                ],
                "travelerPricings": [
                    {
                        "travelerId": "1",
                        "fareOption": "STANDARD",
                        "travelerType": "ADULT",
                        "price": {
                            "currency": "EUR",
                            "total": "218.08",
                            "base": "121.00",
                            "taxes": [
                                {
                                    "amount": "40.00",
                                    "code": "O4"
                                },
                                {
                                    "amount": "5.83",
                                    "code": "WL"
                                },
                                {
                                    "amount": "13.95",
                                    "code": "QX"
                                },
                                {
                                    "amount": "22.30",
                                    "code": "FR"
                                },
                                {
                                    "amount": "0.90",
                                    "code": "XU"
                                },
                                {
                                    "amount": "14.10",
                                    "code": "BP"
                                }
                            ],
                            "refundableTaxes": "97.08"
                        },
                        "fareDetailsBySegment": [
                            {
                                "segmentId": "1",
                                "cabin": "ECONOMY",
                                "fareBasis": "YCNV1",
                                "class": "Y",
                                "includedCheckedBags": {
                                    "quantity": 1
                                }
                            },
                            {
                                "segmentId": "2",
                                "cabin": "ECONOMY",
                                "fareBasis": "YCNV1",
                                "class": "Y",
                                "includedCheckedBags": {
                                    "quantity": 1
                                }
                            },
                            {
                                "segmentId": "3",
                                "cabin": "ECONOMY",
                                "fareBasis": "YCNV1",
                                "class": "Y",
                                "includedCheckedBags": {
                                    "quantity": 1
                                }
                            }
                        ]
                    },
                    {
                        "travelerId": "2",
                        "fareOption": "STANDARD",
                        "travelerType": "ADULT",
                        "price": {
                            "currency": "EUR",
                            "total": "218.08",
                            "base": "121.00",
                            "taxes": [
                                {
                                    "amount": "40.00",
                                    "code": "O4"
                                },
                                {
                                    "amount": "5.83",
                                    "code": "WL"
                                },
                                {
                                    "amount": "13.95",
                                    "code": "QX"
                                },
                                {
                                    "amount": "22.30",
                                    "code": "FR"
                                },
                                {
                                    "amount": "0.90",
                                    "code": "XU"
                                },
                                {
                                    "amount": "14.10",
                                    "code": "BP"
                                }
                            ],
                            "refundableTaxes": "97.08"
                        },
                        "fareDetailsBySegment": [
                            {
                                "segmentId": "1",
                                "cabin": "ECONOMY",
                                "fareBasis": "YCNV1",
                                "class": "Y",
                                "includedCheckedBags": {
                                    "quantity": 1
                                }
                            },
                            {
                                "segmentId": "2",
                                "cabin": "ECONOMY",
                                "fareBasis": "YCNV1",
                                "class": "Y",
                                "includedCheckedBags": {
                                    "quantity": 1
                                }
                            },
                            {
                                "segmentId": "3",
                                "cabin": "ECONOMY",
                                "fareBasis": "YCNV1",
                                "class": "Y",
                                "includedCheckedBags": {
                                    "quantity": 1
                                }
                            }
                        ]
                    }
                ]
            }
        ],
        "bookingRequirements": {
            "emailAddressRequired": true,
            "mobilePhoneNumberRequired": true
        }
    },
    "dictionaries": {
        "locations": {
            "ICN": {
                "cityCode": "SEL",
                "countryCode": "KR"
            },
            "CDG": {
                "cityCode": "PAR",
                "countryCode": "FR"
            },
            "HEL": {
                "cityCode": "HEL",
                "countryCode": "FI"
            }
        }
    }
}

+++++
# booking order. here passenger details are added
{
  "type": "flight-offer",
  "id": "1",
  "source": "GDS",
  "instantTicketingRequired": false,
  "nonHomogeneous": false,
  "paymentCardRequired": false,
  "lastTicketingDate": "2025-11-30",
  "itineraries": [
    {
      "segments": [
        {
          "departure": {
            "iataCode": "CDG",
            "at": "2025-11-30T15:25:00"
          },
          "arrival": {
            "iataCode": "HEL",
            "at": "2025-11-30T19:20:00"
          },
          "carrierCode": "6X",
          "number": "3618",
          "aircraft": {
            "code": "733"
          },
          "operating": {
            "carrierCode": "6X"
          },
          "duration": "PT2H55M",
          "id": "1",
          "numberOfStops": 0,
          "co2Emissions": [
            {
              "weight": 175,
              "weightUnit": "KG",
              "cabin": "ECONOMY"
            }
          ]
        },
        {
          "departure": {
            "iataCode": "HEL",
            "at": "2025-12-01T17:30:00"
          },
          "arrival": {
            "iataCode": "ICN",
            "at": "2025-12-02T08:20:00"
          },
          "carrierCode": "6X",
          "number": "3605",
          "aircraft": {
            "code": "733"
          },
          "operating": {
            "carrierCode": "6X"
          },
          "duration": "PT7H50M",
          "id": "2",
          "numberOfStops": 0,
          "co2Emissions": [
            {
              "weight": 295,
              "weightUnit": "KG",
              "cabin": "ECONOMY"
            }
          ]
        }
      ]
    },
    {
      "segments": [
        {
          "departure": {
            "iataCode": "ICN",
            "at": "2025-12-14T09:53:00"
          },
          "arrival": {
            "iataCode": "CDG",
            "at": "2025-12-14T14:10:00"
          },
          "carrierCode": "6X",
          "number": "957",
          "aircraft": {
            "code": "332"
          },
          "operating": {
            "carrierCode": "6X"
          },
          "duration": "PT12H17M",
          "id": "3",
          "numberOfStops": 0,
          "co2Emissions": [
            {
              "weight": 381,
              "weightUnit": "KG",
              "cabin": "ECONOMY"
            }
          ]
        }
      ]
    }
  ],
  "price": {
    "currency": "EUR",
    "total": "436.16",
    "base": "242.00",
    "fees": [
      {
        "amount": "0.00",
        "type": "SUPPLIER"
      },
      {
        "amount": "0.00",
        "type": "TICKETING"
      },
      {
        "amount": "0.00",
        "type": "FORM_OF_PAYMENT"
      }
    ],
    "grandTotal": "436.16",
    "billingCurrency": "EUR"
  },
  "pricingOptions": {
    "fareType": [
      "PUBLISHED"
    ],
    "includedCheckedBagsOnly": true
  },
  "validatingAirlineCodes": [
    "6X"
  ],
  "travelerPricings": [
    {
      "travelerId": "1",
      "fareOption": "STANDARD",
      "travelerType": "ADULT",
      "price": {
        "currency": "EUR",
        "total": "218.08",
        "base": "121.00",
        "taxes": [
          {
            "amount": "40.00",
            "code": "O4"
          },
          {
            "amount": "5.83",
            "code": "WL"
          },
          {
            "amount": "13.95",
            "code": "QX"
          },
          {
            "amount": "22.30",
            "code": "FR"
          },
          {
            "amount": "0.90",
            "code": "XU"
          },
          {
            "amount": "14.10",
            "code": "BP"
          }
        ],
        "refundableTaxes": "97.08"
      },
      "fareDetailsBySegment": [
        {
          "segmentId": "1",
          "cabin": "ECONOMY",
          "fareBasis": "YCNV1",
          "class": "Y",
          "includedCheckedBags": {
            "quantity": 1
          }
        },
        {
          "segmentId": "2",
          "cabin": "ECONOMY",
          "fareBasis": "YCNV1",
          "class": "Y",
          "includedCheckedBags": {
            "quantity": 1
          }
        },
        {
          "segmentId": "3",
          "cabin": "ECONOMY",
          "fareBasis": "YCNV1",
          "class": "Y",
          "includedCheckedBags": {
            "quantity": 1
          }
        }
      ]
    },
    {
      "travelerId": "2",
      "fareOption": "STANDARD",
      "travelerType": "ADULT",
      "price": {
        "currency": "EUR",
        "total": "218.08",
        "base": "121.00",
        "taxes": [
          {
            "amount": "40.00",
            "code": "O4"
          },
          {
            "amount": "5.83",
            "code": "WL"
          },
          {
            "amount": "13.95",
            "code": "QX"
          },
          {
            "amount": "22.30",
            "code": "FR"
          },
          {
            "amount": "0.90",
            "code": "XU"
          },
          {
            "amount": "14.10",
            "code": "BP"
          }
        ],
        "refundableTaxes": "97.08"
      },
      "fareDetailsBySegment": [
        {
          "segmentId": "1",
          "cabin": "ECONOMY",
          "fareBasis": "YCNV1",
          "class": "Y",
          "includedCheckedBags": {
            "quantity": 1
          }
        },
        {
          "segmentId": "2",
          "cabin": "ECONOMY",
          "fareBasis": "YCNV1",
          "class": "Y",
          "includedCheckedBags": {
            "quantity": 1
          }
        },
        {
          "segmentId": "3",
          "cabin": "ECONOMY",
          "fareBasis": "YCNV1",
          "class": "Y",
          "includedCheckedBags": {
            "quantity": 1
          }
        }
      ]
    }
  ]
}
```
