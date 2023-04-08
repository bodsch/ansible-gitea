"""
  upgrade gitea:

  see: https://github.com/go-gitea/gitea/blob/main/contrib/upgrade.sh

# stop gitea, create backup, replace binary, restart gitea
echo "Flushing gitea queues at $(date)"
giteacmd manager flush-queues
echo "Stopping gitea at $(date)"
$service_stop
echo "Creating backup in $giteahome"
giteacmd dump $backupopts
echo "Updating binary at $giteabin"
cp -f "$giteabin" "$giteabin.bak" && mv -f "$binname" "$giteabin"
$service_start
$service_status
"""
