# Princeton Walking

Welcome to the Princeton Walking Repositiory

## Goals
The goal of this repo to answer a basic question from the Mayor:

<i> Not sure if all the info would be ready in time to make this work, but I'd love to be able to say that x percentage of residents live within a 10 minute walk of a park or open space. Is it possible to build a program using the GIS data that would calculate that? If so, that would be a great planning tool! </i>

## Ideas for Data Usage
Suggest some!

Collaborative GDoc - https://docs.google.com/document/d/1__fNmBh4hsyK-LsRpkj0DrmFNUGX8-QHwIp7VwVHMow/edit

Some starting thoughts posted here...

## Data
- variable: 10 minutes walking = ~800 meters at ~5kph
- parks: locations needed
- residents' locations: 
  - not available, households could be proxy but also not available
  - street addresses: complete address listings available - use as proxy
- address info includes zone of address - e.g. residential vs commercial

## Parks
- create parks "point" OSM layer (use #osm team to do?)
- create parks "shape" OSM layer (use #osm team to do?)
- create test versions of both and let #osm team complete
- use OSM tool to create a square shape X meters around the point, then circle tool to extend
- ...

## Street Addresses
- convert XLS to CSV
- cleanup zone column - extract R (Residential vs other)
- geocode street locations to latlong
- convert to proper OSM format or JSON for import
- ...

## Analysis
Steps

- Make dataset of pins for each park.
- Add circle of X meters around each.
- Look at overlap.

Do parks points with 800m circle cover 100% of the town? 
  - If so, then investigate min circle size to cover whole town?
  - If not, perhaps spark discussion of where to add open space?

Then:
- Change X interactively to find overlap "Venn" style circles that overlap 100% of town.
- Set a goal of Z meters for town.
-  Is Z > or < than X?

## Questions
- Are we trying to solve for something else? Avg distance to park?
- Is a park a point (easier for distance) or a polygon
   - need distance point to poly, or ability to extend a polygon out 
- Is passive open space the same as parks?

## Next
What are other interesting questions we can ask if we had other geo point sets and street addresses? 

For example, response time for emergency services, access to nearest bike paths, ...

## Usage Notes
- Download or fork here to start contributing
- If there are any comments, issues, or suggestions please open an Issue through the tab on the right

## Original Dataset
The original dataset is located under <b> originalDataset </b> and contains the Zones, Acrage, and Addresses
