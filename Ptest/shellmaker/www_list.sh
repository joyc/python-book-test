
#!/bin/sh
################################################################################
# SCRIPT NAME        : file_backup_sync.sh
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
while :
do
if [ -f ~/job/watcher_started.txt ]; then
		break
	else
		sleep 10s
	fi
done

# Copy files to the backup area.
echo `date '+%Y/%m/%d %H:%M:%S'`" [Start] File backup - alaya" >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

# Start backing up "alaya" directory.
echo `date '+%Y/%m/%d %H:%M:%S'`" [Start] Backup "cms/alaya" directory" >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?


sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/applications/ $BK_ALAYA_DIR/alaya/applications >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/applications\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/mhlw_kourou/content/ $BK_ALAYA_DIR/alaya/customer/mhlw_kourou/content >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/mhlw_kourou/content\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/alaya/template/ $BK_ALAYA_DIR/alaya/customer/alaya/template >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/alaya/template\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/alaya/*.properties $BK_ALAYA_DIR/alaya/customer/alaya/template >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/alaya/template\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/alaya/*.xml $BK_ALAYA_DIR/alaya/customer/alaya/template >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/alaya/template\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/WEB-INF/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/WEB-INF >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/WEB-INF\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/alaya/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/alaya >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/alaya\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/wysiwyg/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/wysiwyg >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/wysiwyg\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/*.* $BK_ALAYA_DIR/tomcat/webapp/ROOT/*.* >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/*.*\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

echo `date '+%Y/%m/%d %H:%M:%S'`" [End] Backup "tomcat/webapps" directory" >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

echo `date '+%Y/%m/%d %H:%M:%S'`" [End] File backup - alaya" >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

touch ~/job/switch2.txt
check_error $?

logger [Not_Notify] ${0#*/} 正常終了
check_error $?
exit 0
