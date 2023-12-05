# Final_Project_CS122

Project Title: Weather App

Authors: Bao Nguyen, Huu Ho

Project Description:
1. The Weather App will be designed with a user-friendly interface.
2. It is designed to provide users with current weather data for any area in the world.
3. In order to guarantee accuracy and timeliness, this application will draw its data from
   reliable online weather APIs.
4. Users easily access data including such as the current temperature, humidity, wind speed,
   description, and pressure.
5. Delving deeper, the app will provide a 5-day weather forecast of that area.

Project Outline/Plan:
Interface Plan
1. Dashboard
   a. Search bar to enter the desired location.
3. Detailed Forecast
   a. Show detailed forecasts for temperature, humidity, wind speed, description, and
   pressure.
4. 5-Day Forecast Page
   a. Card view for next 5-day showing minimum and maximum temperature.
5. Plotting Feature
   a. Utilizing the capabilities of the matplotlib.pyplot and scipy.interpolate modules to enhance our data visualization.
   b. Interpreting temperature trends over the next 10 hours of the current input city, ensuring users have a detailed view of temperature changes.
   c. The graph includes time on the x-axis, temperature on the y-axis, and each data point is annotated with the corresponding temperature value

Data Collection (written by Bao Nguyen)
1. Data Collection
  a. Integration with OpenWeatherMap API ensures reliable and up-to-date data.
  b. Utilize periodic fetching to guarantee current data.

Data Analysis and Visualization Plan (written by Huu Ho)
1. Data Analysis
  a. Seamless integration with the OpenWeatherMap API, allowing us to retrieve comprehensive weather data, including temperature, wind speed, humidity, and more
  b. Utilizing the TimezoneFinder module to determine the timezone of the selected city, ensuring precise and localized weather information.
2. Visualization Plan
  a. Represent different weather situations using simple icons.
  b. Make sure there is a mix of numerical and graphical data representations for a
     variety of user preferences.
