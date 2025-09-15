# crowdfunding_backend
Django-DRF She Codes Project

# Crowdfunding Back End
Juliane Gutierrez

## Planning:
### Concept/Name
It is a crowndfunding backend website to fund flight tickes to travel to Brazil to see my parents.

### Intended Audience/User Stories
Adults only, mainly immigrats in Australia who understands what life is far from their parents.

### Front End Pages/Functionality
- Homepage
    - Featuredkickstarters
- Create a new fundraiser page 

    - Form with all fundraiser details
    - Ability to submit
    - Nice error pages for validation issues
    - 
- {{ A page on the front end }}
    - {{ A list of dot-points showing functionality is available on this page }}
    - {{ etc }}
    - {{ etc }}
- {{ A second page available on the front end }}
    - {{ Another list of dot-points showing functionality }}
    - {{ etc }}

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}


| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | ----------- | ------- | ------------ | --------------------- | ---------------------------- |
|     |             |         |              |                       |                              |

|URL           | HTTP Method| Purpose| 
 /fundraisers  | GET        | Fetch all the fundraisers 
 /fundraisers/ | POST       | Create a new fundraiser
 /fundraisers/ | GET        | 
 /1pledges/    | GET        | Fetch all pledges
 /1 pledges/   | POST       | New pledge
 /users/       | GET        | Fetch all users
 /users/       | POST       | new user

Request Body  | Success Response Code| Authentication/Authorisation|
 N/A          | 200                 | None
 JSON         | 201                 | Any logged in user 
 N/A          | N/A                 | N/A
 N/A          | 200                 | None
 JSON         | 201                 | Logged in user
 N/A          | 200                 | None
 JSON         | 201                 | Logged in user






# this table needs to be updated

### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )