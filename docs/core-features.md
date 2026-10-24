# Mars Mission Planner: Core Features

NASA Space Apps Challenge · Interplanetary Survival Guide, Martian Map · Submission deadline: November 14

## The big picture

Our app helps an astronaut on Mars pick a safe route. The user clicks two points on the map, and the app shows the safest path, explains why it is safe, and shows what the conditions are like there.

These are the five core features. We build these first. Everything else is a bonus.

## 1. Layer switcher

**What it does:** the user can change how the map looks. One view is a simple colored map showing high and low ground. The other is real photos of the surface. It works like switching between map view and satellite view on Google Maps.

**Data needed:** Mars map tiles from NASA Mars Trek.

**Owner:** Zayem

## 2. Safest route

**What it does:** the user clicks a start point and an end point on the map. The app draws the safest path between them. It avoids steep hills and goes around dangerous ground, even if the trip becomes a bit longer. This is the heart of the project.

**Data needed:** elevation data for the area, which we use to calculate how steep the ground is.

**Owner:** Hussain (with elevation data from Abdullah and click coordinates from Zayem)

## 3. Slope hazard map

**What it does:** the map shows steep areas in red, medium areas in yellow, and flat safe ground in green. This shows people why the route goes around certain places.

**Data needed:** the same slope data we already calculate for the route, so this is almost free.

**Owner:** Hussain calculates the slope, Zayem and the frontend developer display it on the map.

## 4. Route summary

**What it does:** after the route is drawn, a box shows the trip details: how far it is, how steep the worst part is, and a safety score such as Safe or Risky. A small chart shows how the ground goes up and down along the route, like a hiking trail profile.

**Data needed:** the route and slope numbers from feature 2.

**Owner:** Hussain provides the numbers, the frontend developer builds the box and chart.

## 5. Conditions panel

**What it does:** a small panel shows real weather measured by the Perseverance rover on Mars, such as temperature and air pressure, with a chart over time. Each reading shows the day it was measured and where it came from. This is not live weather, and the panel says so clearly.

**Data needed:** archived Perseverance weather instrument (MEDA) data.

**Owner:** Abdullah finds and prepares the data, the frontend developer displays it.

## How it all fits together

1. Zayem's map shows Mars and lets the user click points.
2. Abdullah's data gives us the ground height and the weather readings.
3. Hussain's logic turns ground height into slope, then into a safe route and a safety score.
4. The frontend developer shows everything in a clean, easy-to-use website.

## Bonus features if we have time

- **Travel time advisor:** use the temperature data to suggest the warmest part of the Martian day for travel.
- **Search by name:** type a crater or valley name and the map jumps there, using USGS place names.
- **Photo popups:** click a location and see NASA photos of the area.
- **Seasonal conditions:** a season slider showing typical conditions from the Mars Climate Database, clearly labeled as model output.

## Left for future work

- Showing Perseverance's actual path and science stops
- Sunlight and timing calculations using NASA SPICE data
