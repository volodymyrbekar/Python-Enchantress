docker pull ubuntu 
docker save -o ubuntu.tar ubuntu
tar -xvzf ubuntu.zip    --directory ./extracted_ubuntu_image/ && cd extracted_ubuntu_image/
tar -cvzf ../ubuntu.zip ./*
cd .. && cat ubuntu.zip | docker load