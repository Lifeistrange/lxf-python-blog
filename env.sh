PROJ_DIR=`pwd`
VENV=${PROJ_DIR}/.env

if [ ! -e ${VENV} ];then
    virtualenv ${VENV} -p $(type -p python3)
fi

source ${VENV}/bin/activate 

export PYTHONPATH=${PROJ_DIR}/www/:${PROJ_DIR}
export PROJ_DIR

