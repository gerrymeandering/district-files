from python:3.6.0

RUN apt-get -y update 
RUN apt-get -y install tmux vim git
RUN pip install requests geojson pyrestcli 
RUN pip install git+https://github.com/osgn/python-topojson.git 
RUN pip install git+https://github.com/CartoDB/carto-python.git@1.0.0  
RUN git clone https://github.com/amix/vimrc.git ~/.vim_runtime  
RUN sh ~/.vim_runtime/install_awesome_vimrc.sh  
