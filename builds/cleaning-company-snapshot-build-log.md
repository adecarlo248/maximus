# Cleaning Company Snapshot Build Log

**Location ID:** `qxs3X4jCYse1W18z5H3k`
**Sub-account:** Cleaning company
**Built:** 2026-07-28T14:34:23.449308

## Research / Setup Strategy

Cleaning companies need fast quote response, tight appointment prep, recurring client conversion, review/referral capture, and separate handling for deadline-based work like move-in/move-out, Airbnb turnovers, commercial walkthroughs, and post-construction cleaning.

Core segments supported:
- Residential standard cleaning
- Deep cleaning
- Move-in / move-out cleaning
- Airbnb / short-term rental turnover cleaning
- Commercial cleaning
- Post-construction cleaning
- Recurring weekly / bi-weekly / monthly cleaning

## Created via API

- Custom fields created: 12
- Pipelines created: 0
- Calendars created: 5
- Tags created: 27
- Errors: 26

## Custom Fields

- Lead Source — `400`
- Cleaning Type — `400`
- Service Frequency — `400`
- Property Type — `400`
- Bedrooms — `XQG0DXk7auWC5Ctwz9Te`
- Bathrooms — `8jDA0NsCEMMq0rQmVeL2`
- Approx Square Footage — `mjRjUT1XJQ1ks6FZPMQt`
- Pets On Site — `400`
- Access Instructions — `q7duSNMmAHo4iJGusyx2`
- Priority Areas — `2z4wXp8XL5C5KJ2NBTx3`
- Special Instructions — `f4wuA2NxMS5OVK8zxjXg`
- Preferred Service Date — `FWckGEG8HWuSwE8hWGWN`
- Quote Amount — `XKZGhuNuBXHMahMq93b7`
- Recurring Plan Price — `yPluevOSWWwePUfO24V0`
- Deposit Paid — `400`
- Cleaner Assigned — `2PP8sCLqA0jFXEr2JQTu`
- Review Requested — `400`
- Review Received — `400`
- Referral Requested — `400`
- Recurring Client — `400`
- Last Service Date — `RyaIOMhWDtCibOxlwqh9`
- Next Service Date — `429`
- Airbnb Checkout Time — `429`
- Airbnb Next Check-In Time — `XOLhVqX2w11A4gU30xRH`

## Pipelines

### Cleaning - New Leads — `422`

### Cleaning - Bookings — `422`

### Cleaning - Recurring Clients — `422`

### Cleaning - Airbnb Turnovers — `422`

### Cleaning - Commercial Leads — `422`

## Calendars

- Residential Cleaning (120 min) — `tg9QzRdagIGLNyJtGLal`
- Deep Cleaning / Move-Out Cleaning (240 min) — `ofzJuk3IazBnIIt3nyxH`
- Commercial Walkthrough / Quote Call (30 min) — `6KyW4eAQrNac1pr7sXg0`
- Airbnb Turnover Cleaning (180 min) — `7fAizhtVVu5GgnqZfK5w`
- Post-Construction Walkthrough (30 min) — `xaPlEQxcwlkmhB57Jgri`

## Tags

- new-lead — `XHbmALVaDAHPYCZLWOKD`
- quote-requested — `2vgRyGPI8flWsSX0pbQr`
- cleaning-booked — `429`
- customer-active — `429`
- cold-lead — `429`
- recurring-client — `429`
- recurring-interest — `Zh5Pyk2JCn6jriqcEWlu`
- recurring-upsell-sent — `vodsr2SHiFeMvHbtzEeg`
- review-requested — `KjcqEoWGZ6YOxAXfBBAL`
- review-received — `yAfq86lwcPs05gEyR5Ow`
- referral-requested — `skv4cKs8X4XhtryRyn6r`
- service-residential-cleaning — `q9Rkz02wM52GpWcCQktP`
- service-deep-cleaning — `vNmW9YyIiga9WNuLJGEi`
- service-move-in-out — `wW2VRkR0f4ZTBRLJFqGO`
- service-commercial-cleaning — `ual4Q9Qz4gGkb7GxtPmO`
- service-airbnb-turnover — `ST4BBzZU2iGIAAUqFNvR`
- service-post-construction — `D7UsOSMKFqP6PmKZUC7i`
- service-recurring-cleaning — `roO3p4h53RyeZkXv7hfe`
- service-one-time-cleaning — `Hr7f51JJ6udWdbIkJ7YS`
- airbnb-turnover-booked — `A5jKwRWFiDSbRMMfNCWR`
- recurring-turnover-interest — `rr6A6Sl0zfVzr3Yh8Lsx`
- commercial-cold-lead — `xjwljFvRdUECGALl3y6H`
- post-construction-lead — `ERbIJJNbUg3c6jC4n0yE`
- no-show — `ig4i6X4zwWfKoNuecajE`
- cancelled — `K9M6dsbiAxilI4o6tgN8`
- facebook-lead — `dBxO6HyCXfaRtvL37xsN`
- google-lead — `jpmZsL6Fp92qADxlKwb2`
- website-lead — `6tXPbThmGZAPW9xM7egN`
- referral-lead — `xZQeuDDyXXjZRvpRCNHC`
- phone-lead — `xm5z1Jie2Mj0KbBK9cD3`
- urgent-clean — `kgK4R6phFmownv3yZahg`
- needs-quote — `429`
- quote-sent — `429`
- invoice-sent — `429`
- paid — `429`
- service-complete — `429`

## Manual Configuration Required

- Assign calendars to users/team members
- Set calendar availability / business hours
- Add calendar confirmation/reminder settings if not using workflow reminders
- Enable native Missed Call Text Back on the phone number
- Build automations manually using `builds/cleaning-service-ai-builder-prompts.md`
- Connect Google Business Profile / review link
- Connect payment/invoicing if needed

## Errors

```json
[
  {
    "customField": "Lead Source",
    "status": 400,
    "response": {
      "message": "v.trim is not a function",
      "error": "Bad Request",
      "statusCode": 400,
      "traceId": "07c7c9e1-9386-4423-b9e8-2c9f5f70d570"
    }
  },
  {
    "customField": "Cleaning Type",
    "status": 400,
    "response": {
      "message": "v.trim is not a function",
      "error": "Bad Request",
      "statusCode": 400,
      "traceId": "4dc2d718-156b-4500-89e9-63613fbe4d14"
    }
  },
  {
    "customField": "Service Frequency",
    "status": 400,
    "response": {
      "message": "v.trim is not a function",
      "error": "Bad Request",
      "statusCode": 400,
      "traceId": "7cb53589-aa06-4dec-84c1-0db012389aa1"
    }
  },
  {
    "customField": "Property Type",
    "status": 400,
    "response": {
      "message": "v.trim is not a function",
      "error": "Bad Request",
      "statusCode": 400,
      "traceId": "2f482291-8e3c-4a62-8862-10b889d8edec"
    }
  },
  {
    "customField": "Pets On Site",
    "status": 400,
    "response": {
      "message": "v.trim is not a function",
      "error": "Bad Request",
      "statusCode": 400,
      "traceId": "4f769a73-7ad2-4af8-95b6-dea1e8ff1931"
    }
  },
  {
    "customField": "Deposit Paid",
    "status": 400,
    "response": {
      "message": "v.trim is not a function",
      "error": "Bad Request",
      "statusCode": 400,
      "traceId": "b0c18fd7-109f-422e-8b02-e7443298b122"
    }
  },
  {
    "customField": "Review Requested",
    "status": 400,
    "response": {
      "message": "v.trim is not a function",
      "error": "Bad Request",
      "statusCode": 400,
      "traceId": "3aff18a8-0883-4c66-b215-bd4ec3ab2be0"
    }
  },
  {
    "customField": "Review Received",
    "status": 400,
    "response": {
      "message": "v.trim is not a function",
      "error": "Bad Request",
      "statusCode": 400,
      "traceId": "075d0b54-f17b-485d-ba59-1a8efb5d7d9c"
    }
  },
  {
    "customField": "Referral Requested",
    "status": 400,
    "response": {
      "message": "v.trim is not a function",
      "error": "Bad Request",
      "statusCode": 400,
      "traceId": "33d89ada-b592-46e9-bf08-344d135a39ee"
    }
  },
  {
    "customField": "Recurring Client",
    "status": 400,
    "response": {
      "message": "v.trim is not a function",
      "error": "Bad Request",
      "statusCode": 400,
      "traceId": "7865bf28-26ad-4f95-9004-8db8621864cd"
    }
  },
  {
    "customField": "Next Service Date",
    "status": 429,
    "response": {
      "statusCode": 429,
      "message": "Too Many Requests"
    }
  },
  {
    "customField": "Airbnb Checkout Time",
    "status": 429,
    "response": {
      "statusCode": 429,
      "message": "Too Many Requests"
    }
  },
  {
    "pipeline": "Cleaning - New Leads",
    "status": 422,
    "response": {
      "message": [
        "stages must contain at least 1 elements",
        "stages must be an array",
        "stages should not be empty"
      ],
      "error": "Unprocessable Entity",
      "statusCode": 422,
      "traceId": "1c67889e-f713-4b39-b90d-cb9f8a052721"
    }
  },
  {
    "pipeline": "Cleaning - Bookings",
    "status": 422,
    "response": {
      "message": [
        "stages must contain at least 1 elements",
        "stages must be an array",
        "stages should not be empty"
      ],
      "error": "Unprocessable Entity",
      "statusCode": 422,
      "traceId": "3fef011f-4095-41aa-aa60-08c362198b50"
    }
  },
  {
    "pipeline": "Cleaning - Recurring Clients",
    "status": 422,
    "response": {
      "message": [
        "stages must contain at least 1 elements",
        "stages must be an array",
        "stages should not be empty"
      ],
      "error": "Unprocessable Entity",
      "statusCode": 422,
      "traceId": "a0791672-abeb-456d-9c54-6236ddb916b1"
    }
  },
  {
    "pipeline": "Cleaning - Airbnb Turnovers",
    "status": 422,
    "response": {
      "message": [
        "stages must contain at least 1 elements",
        "stages must be an array",
        "stages should not be empty"
      ],
      "error": "Unprocessable Entity",
      "statusCode": 422,
      "traceId": "32655765-8999-4bf2-96d8-a12e0e6019de"
    }
  },
  {
    "pipeline": "Cleaning - Commercial Leads",
    "status": 422,
    "response": {
      "message": [
        "stages must contain at least 1 elements",
        "stages must be an array",
        "stages should not be empty"
      ],
      "error": "Unprocessable Entity",
      "statusCode": 422,
      "traceId": "13cc6265-4820-4ad2-b5b4-c37fd8ae41dd"
    }
  },
  {
    "tag": "cleaning-booked",
    "status": 429,
    "response": {
      "statusCode": 429,
      "message": "Too Many Requests"
    }
  },
  {
    "tag": "customer-active",
    "status": 429,
    "response": {
      "statusCode": 429,
      "message": "Too Many Requests"
    }
  },
  {
    "tag": "cold-lead",
    "status": 429,
    "response": {
      "statusCode": 429,
      "message": "Too Many Requests"
    }
  },
  {
    "tag": "recurring-client",
    "status": 429,
    "response": {
      "statusCode": 429,
      "message": "Too Many Requests"
    }
  },
  {
    "tag": "needs-quote",
    "status": 429,
    "response": {
      "statusCode": 429,
      "message": "Too Many Requests"
    }
  },
  {
    "tag": "quote-sent",
    "status": 429,
    "response": {
      "statusCode": 429,
      "message": "Too Many Requests"
    }
  },
  {
    "tag": "invoice-sent",
    "status": 429,
    "response": {
      "statusCode": 429,
      "message": "Too Many Requests"
    }
  },
  {
    "tag": "paid",
    "status": 429,
    "response": {
      "statusCode": 429,
      "message": "Too Many Requests"
    }
  },
  {
    "tag": "service-complete",
    "status": 429,
    "response": {
      "statusCode": 429,
      "message": "Too Many Requests"
    }
  }
]
```
