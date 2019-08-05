FROM championape/jupyterlab-docker:ca749818963f58ed0f50a7db201e1fc96fdae6e2
# The tag is the last commit tag in jupyterlab-docker

# Make sure the contents of our repo are in ${HOME} 
COPY . ${HOME}

USER root

RUN fix-permissions ${HOME}

# Install conda deps
RUN if [ -e environment.yml ]; then \
      conda env update -f environment.yml; \
    fi

# Run script if present
RUN if [ -e script.sh ]; then \
      bash script.sh; \
    fi
