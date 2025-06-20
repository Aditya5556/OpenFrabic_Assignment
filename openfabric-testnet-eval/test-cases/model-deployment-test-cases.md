# Test Cases for Model Deployment

| TC_ID  | Description                                 | Steps                                               | Expected Outcome             | Type     |
|--------|---------------------------------------------|-----------------------------------------------------|------------------------------|----------|
| TC_01  | Validate successful login via wallet        | Go to login page → Click Metamask login → Approve   | User lands on dashboard      | Positive |
| TC_02  | Model deploy with valid inputs              | Open deploy form → Fill valid URL → Submit          | Deployment success message   | Positive |
| TC_03  | Model deploy with empty input               | Submit with empty model URL                         | Form shows validation error  | Negative |
| TC_04  | Deploy model without enough funds           | Faucet not used → Try deploy                        | Alert: Insufficient tokens   | Negative |
| TC_05  | Chain AI agents with mismatched ontologies  | Connect two incompatible models                     | Error about schema mismatch  | Edge     |
// open preview to see table