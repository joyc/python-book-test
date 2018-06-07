
#!/bin/sh
################################################################################
# SCRIPT NAME        : {}.sh
# SCRIPT DESCRIPTION : ファイル用バックアップ
# OPTION             : N/A
# ARGUMENT           : $1 = 何でも可
# RETURN             : 0       :       正常終了
#                    : 1       :       引数異常
################################################################################
# Ver. When        Who               Description
# 1.0  2018/06/04  ACN tanaka         初回リリース
################################################################################ 

# 設定ファイルを読み込み
. ./alaya_conf.sh

# check if job_watcher has started
# while :
# do
# if [ -f ~/job/watcher_started.txt ]; then
# 		break
# 	else
# 		sleep 10s
# 	fi
# done

# Begin file sync to DR server.
sudo echo `date '+%Y/%m/%d %H:%M:%S'`" [Start] Sync files to DR server" >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/content/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/content >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"$ALAYA_BAR_DIR/content\" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/*.properties alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/content >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"$ALAYA_BAR_DIR/content\" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya/$ALAYA_DIR_TOMCAT/WEB-INF/ alaya@$IP_ADDRESS:$ALAYA_DIR_TOMCAT/WEB-INF >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"$ALAYA_DIR_TOMCAT/WEB-INF\" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya/$ALAYA_DIR_TOMCAT/*.* alaya@$IP_ADDRESS:$ALAYA_DIR_TOMCAT/*.* >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"$ALAYA_DIR_TOMCAT/*.*\" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

# Closing file sync to DR server.
sudo echo `date '+%Y/%m/%d %H:%M:%S'`" [End] Sync files to DR server" >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

logger [Not_Notify] ${0#*/} 正常終了
check_error $?
exit 0
