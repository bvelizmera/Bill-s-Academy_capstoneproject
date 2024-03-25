# TESTING
<br>
## Functional Testing
Different features were tested during this process and the results can be observed on table 1.

![features tested](documentation/testing/features%20tested.png) 
 - Table 1


## Code Validation

### HTML

As recommended, [HTML W3C Validator](https://validator.w3.org) was used to validate HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| tournament/templates/tournament | new_list.html | ![screenshot](documentation/testing/home-w3c.png) | 1 error present on all pages - it comes from the fontawesome kit: transform: var(--fa-rotate-angle, none)|
| tournament/templates/tournament | tournament_list.html | ![screenshot](documentation/testing/tournamentsw3c-.png) | 1 error present on all pages - it comes from the fontawesome kit: transform: var(--fa-rotate-angle, none)|

While going through validation and testing I realised that I did not follow standard normalisation procedures, since I had used ID's to style different elements which makes it bad pratice, after that I fixed the html for the project thus resulting in only the problems mentioned above which one is just not adding the "<!DOCTYPE html>" tag on the validator, but ensured it is present on the document.

Below you will be able to see some of the problems that occured with duplication of ID. I also did not put assign an alt value to the images before. [bad practice html](documentation/testing/Duplication%20of%20ID.png)


### CSS

As recommended, [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) was used to validate the css file.


| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static/css | style.css | ![screenshot](documentation/testing/css-w3c.png)| No errors |

### Python

As recommended by the programme, [CI Python Linter](https://pep8ci.herokuapp.com) was used for Python validation.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| tennisacademy | urls.py |  ![screenshot](documentation/testing/urls-py.png) |
| tournament | models.py |  ![screenshot](documentation/testing/models-py.png) |
| tournament | forms.py |  ![screenshot](documentation/testing/forms-py.png) |
| tournament | urls.py |  ![screenshot](documentation/testing/urls-tourn-py.png) |
| tournament | views.py |  ![screenshot](documentation/testing/views-py.png) | Only errors with length |
| tournament | admin.py |  ![screenshot](documentation/testing/admin-py.png) |

### No JavaScript was used for this project apart from the predetermined script for the navbar.


## Browser Compatibility

I've tested my deployed project on the main 3 browsers to check for compatibility issues.

| Browser | Screenshot | Intended Appearance | Intended Responsivity |
| --- | --- | --- | --- |
| Chrome| ![screenshot](documentation/testing/chrome.png) | Good | Good |
| Firefox| ![screenshot](documentation/testing/firefox.png) | Good | Good |
| Edge| ![screenshot](documentation/testing/edge.png) | Good | Good |


## Lighthouse Audit

Lighthouse Audit tool was used to test the deployed proyect. Overall, the website performed better on deskptop but sacrificed accesibility.

However, there is only one parameter that is low on mobile, which is the performance, this can be improved by reducing the size of the images(compression), eliminate render-blocking resources and reducing resources overall that slow down the loading times.

The website performed on average with the parameters shown as follows:

### Phone
![Phone Lighthouse](documentation/testing/lighthouse-phone.png)

### Desktop
![Desktop Lighthouse](documentation/testing/lighthouse-desktop.png)


## Defensive Programming

Defensive was carried to ensure a smoother experience on the website. The following tables show as follows.

![Table 2](documentation/testing/home,%20tournaments,%20news.png)
![Table 3](documentation/testing/Profile,%20Edit%20Profile,%20Add%20Tournament,%20Add%20News,%20Register,%20Log%20In,%20Log%20Out.png)

## Responsiveness

The responsiveness tests the layout flexibility to adapt smoothly to different screen sizes.

In this case, it was tested by using Google Dev Tools. To carry out the responsiveness test, it is necessary to:

1. Right click on the website
2. Click on inspect element.
3. Then in the middle of the page, it will show the screen size, and we can select the preferred option. In this case, responsive was chosen to drag and see how it behaves for different screen sizes.

