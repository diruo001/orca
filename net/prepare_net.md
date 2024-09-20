### download 
```
wget https://github.com/zhongfly/Clash-premium-backup/releases/download/2023-09-05-gdcc8d87/clash-linux-amd64-n2023-09-05-gdcc8d87.gz
gzip -d clash-linux-amd64-n2023-09-05-gdcc8d87.gz 
chmod +x clash-linux-amd64-n2023-09-05-gdcc8d87
mv clash-linux-amd64-n2023-09-05-gdcc8d87 clash
```
### start clash service
```
cp clash.service /etc/systemd/system/
systemctl daemon-reload
systemctl start clash
```
查询clash service状态
`systemctl status clash`
### active clash port
```
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
```