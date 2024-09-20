# orca

## install

download orca
```
pip install  -r requirement.txt
python main.py download --orca
```
unzip   
```
tar -Jxvf orca.tar.xz
mv orca_5_0_4_linux_x86-64_shared_openmpi411 ORCA-5.0.4
```
install openmpi
```
wget https://download.open-mpi.org/release/open-mpi/v4.1/openmpi-4.1.1.tar.gz
tar xvf openmpi-4.1.1.tar.gz
cd openmpi-4.1.1
mkdir build
cd build
../configure --prefix=/data/software/openmpi411
make
make install

```
environment variable setting
```
export PATH=$PATH:/data/software/openmpi411/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/data/software/openmpi411/lib

export PATH=$PATH:/data/software/ORCA-5.0.4
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/data/software/ORCA-5.0.4
alias orca=/data/software/ORCA-5.0.4/orca

```
or
```
cat env.txt >> ~/.bashrc
bash ~/.bashrc
```
