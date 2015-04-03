# Database Overview

### Collections
* users (user data)
```
{
    uni:
    email:
    first_name:
    last_name:
}
```
* listed (user-listed sections)
```
{
    uni:                // should correspond with users
    CallNumber:         // should correspond with courses
    status:             // open, pending, closed
}
* courses (course data from CUIT)
```
For "Course":
    contains "SCNC1100" // FroSci
    contains "HUMA1121" // ArtHum
    contains "HUMA1123" // MusicHum
    contains "HUMA1001" // LitHum I
    contains "HUMA1002" // LitHum II
    contains "COCI1101" // CC I
    contains "COCI1102" // CC II
    contains "ENGL1010" // UWriting
             "ENGL1011"
             "ENGL1012"
             "ENGL1013"
             "ENGL1014"
             "ENGL1020"
```