#!/bin/bash
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

ERROR=${RED}[ERROR]${NC}
SUCCESS=${GREEN}[SUCCESS]${NC}
INFO=${CYAN}[INFO]${NC}

PYTHON_DIRECTORY_LOCAL='/usr/local/bin/python2.7'
PYTHON_DIRECTORY_LOCAL_1='/usr/local/lib/python2.7.9'
PYTHON_DIRECTORY='/usr/bin/python2.7'

echo  -e ${INFO} "-----Creating Virtual Environment-----"
if [ -f ${PYTHON_DIRECTORY_LOCAL} ];
then
  echo ${PYTHON_DIRECTORY_LOCAL}
  virtualenv -p ${PYTHON_DIRECTORY_LOCAL} cuckoo_virtual_env
elif [  -f ${PYTHON_DIRECTORY_LOCAL_1} ]
then
  echo ${PYTHON_DIRECTORY_LOCAL_1}
  virtualenv -p ${PYTHON_DIRECTORY_LOCAL_1} cuckoo_virtual_env
else
  echo ${PYTHON_DIRECTORY}
  virtualenv -p ${PYTHON_DIRECTORY} cuckoo_virtual_env
fi
echo  -e ${INFO} "-----Virtual Environment Created-----"
source cuckoo_virtual_env/bin/activate
echo  -e ${INFO} "Installing requirements.."
echo -e ${CYAN}
echo | cat requirements.txt
echo -e ${NC}
pip install -r requirements.txt
deactivate