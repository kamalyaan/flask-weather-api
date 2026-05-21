# Weather API 🌡️ | Built on Android

REST API serving JSON weather data. Built 100% on mobile using Pydroid 3. No laptop used.

### **Tech Stack**
- **Language:** Python 3
- **Framework:** Flask 
- **Platform:** Android (Pydroid 3)

### **API Endpoints**
| Method | Route | Description |
| --- | --- | --- |
| GET | `/` | Returns welcome message |
| GET | `/garmi` | Returns temp data as JSON |

### **Sample Response**
```json
{
  "temp": "41°C",
  "location": "New Chandigarh",
  "status": "Backend Developer in Progress"
}
