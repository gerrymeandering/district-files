# Historical District Files
This is a repo for US historical district shapes along with various Gerymandering scores. Data was combiled by [Levi Wolf](http://ljwolf.org/) and 
can be found [here](https://osf.io/mjvkb/)

Files are formated and avalibale through [git-LFS](https://git-lfs.github.com/).   

## Visualization 

The data can be visualised by the [d3 based viewer](http://gerrymeandering.com/district-viewer/) ( [repo](https://github.com/gerrymeandering/district-viewer) 
or on Carto as an interactive [dashboard](https://team.carto.com/u/stuartlynn/builder/3d954024-e262-11e6-aed1-0ecd1babdde5/embed) 

## Generating the files
Code to extract geojson files from CARTO and make them avaliable as static geojson/topojson files by state

RUN using Docker 

```bash
docker build -t districts .
docker run -it --tm -v $(PWD):/data districts python  /data/download_from_carto.py 
```



