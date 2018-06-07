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
echo `date '+%Y/%m/%d %H:%M:%S'`" [Start] Backup \"cms/alaya\" directory" >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

# automake by pyshell 
# start ---->

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/applications/ $BK_ALAYA_DIR/alaya/applications >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/applications\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/mhlw_kourou/content/ $BK_ALAYA_DIR/alaya/customer/mhlw_kourou/content >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/mhlw_kourou/content\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/mhlw_kourou/expimp/ $BK_ALAYA_DIR/alaya/customer/mhlw_kourou/expimp >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/mhlw_kourou/expimp\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/mhlw_kourou/file/ $BK_ALAYA_DIR/alaya/customer/mhlw_kourou/file >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/mhlw_kourou/file\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/mhlw_kourou/html/ $BK_ALAYA_DIR/alaya/customer/mhlw_kourou/html >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/mhlw_kourou/html\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/mhlw_kourou/image/ $BK_ALAYA_DIR/alaya/customer/mhlw_kourou/image >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/mhlw_kourou/image\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/mhlw_kourou/js/ $BK_ALAYA_DIR/alaya/customer/mhlw_kourou/js >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/mhlw_kourou/js\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/mhlw_kourou/plugins/ $BK_ALAYA_DIR/alaya/customer/mhlw_kourou/plugins >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/mhlw_kourou/plugins\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/mhlw_kourou/styleshee/ $BK_ALAYA_DIR/alaya/customer/mhlw_kourou/styleshee >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/mhlw_kourou/styleshee\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/mhlw_kourou/template/ $BK_ALAYA_DIR/alaya/customer/mhlw_kourou/template >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/mhlw_kourou/template\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/mhlw_kourou/temporary/ $BK_ALAYA_DIR/alaya/customer/mhlw_kourou/temporary >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/mhlw_kourou/temporary\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/mhlw_kourou/*.properties $BK_ALAYA_DIR/alaya/customer/mhlw_kourou/*.propertie >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/mhlw_kourou/*.propertie\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/mhlw_kourou/*.xml $BK_ALAYA_DIR/alaya/customer/mhlw_kourou/*.xm >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/mhlw_kourou/*.xm\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/mcode/ $BK_ALAYA_DIR/alaya/customer/mcode >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/mcode\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/alaya/content/ $BK_ALAYA_DIR/alaya/customer/alaya/content >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/alaya/content\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/alaya/html/ $BK_ALAYA_DIR/alaya/customer/alaya/html >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/alaya/html\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/alaya/image/ $BK_ALAYA_DIR/alaya/customer/alaya/image >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/alaya/image\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/alaya/js/ $BK_ALAYA_DIR/alaya/customer/alaya/js >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/alaya/js\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/alaya/plugins/ $BK_ALAYA_DIR/alaya/customer/alaya/plugins >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/alaya/plugins\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/alaya/stylesheet/ $BK_ALAYA_DIR/alaya/customer/alaya/stylesheet >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/alaya/stylesheet\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/alaya/template/ $BK_ALAYA_DIR/alaya/customer/alaya/template >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/alaya/template\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/alaya/temporary/ $BK_ALAYA_DIR/alaya/customer/alaya/temporary >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/alaya/temporary\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/alaya/*.properties $BK_ALAYA_DIR/alaya/customer/alaya/*.properties >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/alaya/*.properties\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/alaya/customer/alaya/*.xml $BK_ALAYA_DIR/alaya/customer/alaya/*.xml >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/alaya/customer/alaya/*.xml\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

# <---- end
# automake by pyshell

echo `date '+%Y/%m/%d %H:%M:%S'`" [End] Backup \"cms/alaya\" directory" >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?



# Start backing up "tomcat" directory.
echo `date '+%Y/%m/%d %H:%M:%S'`" [Start] Backup \"tomcat/webapps\" directory" >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

# automake by pyshell 
# start ---->

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/WEB-INF/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/WEB-INF >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/WEB-INF\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/accessibility/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/accessibility >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/accessibility\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/alaya/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/alaya >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/alaya\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/bunya/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/bunya >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/bunya\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/chosakuken/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/chosakuken >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/chosakuken\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/closeup/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/closeup >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/closeup\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/common/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/common >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/common\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/content/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/content >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/content\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/douga/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/douga >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/douga\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/etsuranshien/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/etsuranshien >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/etsuranshien\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/facebook/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/facebook >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/facebook\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/file/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/file >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/file\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/houdou_kouhou/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/houdou_kouhou >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/houdou_kouhou\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/image/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/image >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/image\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/info/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/info >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/info\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/jigyo_shiwake/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/jigyo_shiwake >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/jigyo_shiwake\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/kensyu/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/kensyu >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/kensyu\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/kojinjouhouhogo/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/kojinjouhouhogo >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/kojinjouhouhogo\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/kouseiroudoushou/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/kouseiroudoushou >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/kouseiroudoushou\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/link/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/link >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/link\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/m/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/m >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/m\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/mailmagazine/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/mailmagazine >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/mailmagazine\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/migtest/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/migtest >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/migtest\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/mobile/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/mobile >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/mobile\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/mobile_site/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/mobile_site >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/mobile_site\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/otoiawase/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/otoiawase >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/otoiawase\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/photo/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/photo >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/photo\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/photo_report/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/photo_report >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/photo_report\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/qa/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/qa >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/qa\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/rss/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/rss >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/rss\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/seisakunitsuite/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/seisakunitsuite >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/seisakunitsuite\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/shinsai_jouhou/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/shinsai_jouhou >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/shinsai_jouhou\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/shinsei_boshu/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/shinsei_boshu >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/shinsei_boshu\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/shokanhourei/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/shokanhourei >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/shokanhourei\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/sitemap/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/sitemap >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/sitemap\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/ssi/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/ssi >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/ssi\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/stf/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/stf >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/stf\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/tenji/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/tenji >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/tenji\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/theme/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/theme >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/theme\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/topics/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/topics >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/topics\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/toukei_hakusho/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/toukei_hakusho >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/toukei_hakusho\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/tsukaikata/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/tsukaikata >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/tsukaikata\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/twitter/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/twitter >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/twitter\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/wysiwyg/ $BK_ALAYA_DIR/tomcat/webapp/ROOT/wysiwyg >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/wysiwyg\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

#DocumentRoot
sudo rsync -ahv --delete --inplace $ALAYA_DIR/tomcat/webapp/ROOT/*.* $BK_ALAYA_DIR/tomcat/webapp/ROOT/*.* >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \"/tomcat/webapp/ROOT/*.*\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

# <---- end
# automake by pyshell 

echo `date '+%Y/%m/%d %H:%M:%S'`" [End] Backup \"tomcat/webapps\" directory" >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?


echo `date '+%Y/%m/%d %H:%M:%S'`" [End] File backup - alaya" >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

touch ~/job/switch2.txt
check_error $?

logger [Not_Notify] ${0#*/} 正常終了
check_error $?
exit 0
