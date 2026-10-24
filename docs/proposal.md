# Mars Mission Planner: Project Proposal

NASA Space Apps Challenge · Challenge: Interplanetary Survival Guide, Martian Map · Submission deadline: November 14

Prepared by Hussain for the team

## The idea in one minute

We are building a web app that helps an astronaut on Mars decide where to go and whether the trip is safe. Instead of just letting people look at Mars, our map plans a route, scores how risky it is, and shows what the trip will cost in time and resources.

Think of it as a mission planner for Mars, not just a viewer.

## The challenge

NASA asks teams to create a layered, integrated view of a location or route on Mars that combines data from multiple NASA science missions. It should help a human explorer plan and carry out a mission safely and quickly, while also supporting new science.

One well-built location is enough for the challenge, so we do not need to map all of Mars.

## What already exists, and how we are different

- **Mars Trek (NASA JPL):** a data browser where you layer high-resolution Mars data around landing sites.
- **Explore Mars (Esri):** a 3D globe showing canyons, mountains, craters and past mission locations.

Both are great for looking at Mars. Neither helps someone plan a trip. That is our gap.

**Our difference:** a hazard-aware route planner. The user picks a start and an end point, and the app finds the safest path and explains why.

## What the app will do

1. **Interactive Mars map** that you can pan and zoom, with layers you can switch on and off.
2. **Route planner.** Click a start and an end point and the app calculates a path that avoids steep slopes and rough terrain.
3. **Hazard score.** Each route gets a simple safety rating based on the terrain along the way.
4. **Mission dashboard.** Shows distance, estimated travel time, and daylight available, measured in sols (Martian days).
5. **Conditions panel.** Shows real measured conditions such as temperature and pressure from NASA rover data, clearly labeled with how old the data is. There is no live weather feed from Mars, so we will be honest about that.

## Starting area

We will build the app for one small area first. Jezero Crater is our proposed starting point because it has the most data available (Perseverance rover, high-resolution imagery and elevation models). The code will be written so that other areas can be added later just by loading new data.

## Planned tech stack

- **Frontend:** React with Vite (final choice made by our frontend developer)
- **Map:** Leaflet with Mars Trek tile layers
- **Routing logic:** JavaScript or TypeScript running in the browser, using an A* pathfinding algorithm over a grid built from elevation data
- **Data preparation:** a small Python script (numpy, rasterio) that converts elevation data into a slope grid, saved as static files together with weather samples
- **Charts:** Chart.js
- **Hosting:** Vercel, Netlify or GitHub Pages, with no backend

Preparing the data in advance and serving it as static files means we do not need a server, which is one less thing that can break before the deadline.

## Data sources to explore

- Mars Trek tile services for map imagery and layers
- USGS Astrogeology for Mars elevation models
- NASA PDS (Planetary Data System) for rover data, including Perseverance weather readings
- NASA Open APIs (api.nasa.gov) for easier JSON data
- Mars Climate Database (ESA/LMD) for typical seasonal conditions
- USGS Gazetteer of Planetary Nomenclature for place names such as craters and valleys

All sources need to be checked for current availability and format.

## Team roles

| Role | Person | What they own |
| --- | --- | --- |
| Routing and hazard logic | Hussain | Slope calculation, pathfinding, route safety score |
| Base map layer | Zayem | Mars map tiles, Leaflet setup, layer toggles, click-to-get-coordinates |
| Data | Abdullah | Elevation data, rover weather samples, a sheet listing every data source |
| Frontend design and build | Our frontend developer | Full website UI, dashboard, overall look and polish |

## Proposed timeline

This is a suggested plan for the roughly three and a half weeks left.

- **By October 28:** base map loads Mars imagery centered on the starting area. Elevation data found and downloaded. Data source sheet finished. Frontend design started.
- **By November 4:** slope grid created from real elevation data. Basic route planner working. Weather sample file ready. Map can return clicked coordinates.
- **By November 10:** everything connected: map, routing, conditions panel and dashboard working together in the frontend.
- **November 11 to 13:** testing, bug fixes, polish, and preparing the project description and demo for submission.
- **November 14:** submit. Aim to finish a day early in case of problems.

## Risks and how we handle them

- **Data is hard to find or messy.** Start data work first and confirm the format early. Fall back to a smaller area if needed.
- **Routing takes longer than expected.** Begin with a simple version (avoid steep slopes only) and add extra factors later.
- **No live Mars weather.** Show recent measured or typical conditions and label the data age.
- **Team members get stuck.** Share progress in the group chat often and ask for help early.
