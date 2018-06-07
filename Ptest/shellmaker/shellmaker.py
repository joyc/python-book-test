#!/usr/bin/env python

# bk_shell
HEADER = """
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
"""
BKHEAD = """
# Copy files to the backup area.
echo `date '+%Y/%m/%d %H:%M:%S'`" [Start] File backup - alaya" >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

# Start backing up "alaya" directory.
echo `date '+%Y/%m/%d %H:%M:%S'`" [Start] Backup \"cms/alaya\" directory" >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?
"""
BKFOOT = """
echo `date '+%Y/%m/%d %H:%M:%S'`" [End] Backup \"tomcat/webapps\" directory" >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

echo `date '+%Y/%m/%d %H:%M:%S'`" [End] File backup - alaya" >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

touch ~/job/switch2.txt
check_error $?

logger [Not_Notify] ${0#*/} 正常終了
check_error $?
exit 0
"""
BCMD_TMP = """
sudo rsync -ahv --delete --inplace $ALAYA_DIR{p1} $BK_ALAYA_DIR{p2} >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \\"{p2}\\" has been backed up." >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?
"""
# middle
MID_TMP = """
echo `date '+%Y/%m/%d %H:%M:%S'`" [End] Backup \"cms/alaya\" directory" >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?

# Start backing up "tomcat" directory.
echo `date '+%Y/%m/%d %H:%M:%S'`" [Start] Backup \"tomcat/webapps\" directory" >> $APP_LOG_DIR/alaya_file_backup.$VAR_DATE.log
check_error $?
"""

# rsync tmp
RSHEAD = """
# Begin file sync to DR server.
sudo echo `date '+%Y/%m/%d %H:%M:%S'`" [Start] Sync files to DR server" >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?
"""
RSFOOT = """
# Closing file sync to DR server.
sudo echo `date '+%Y/%m/%d %H:%M:%S'`" [End] Sync files to DR server" >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

logger [Not_Notify] ${0#*/} 正常終了
check_error $?
exit 0
"""
# rsync alaya
RALA_TMP = """
sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR{r1} alaya@$IP_ADDRESS:$ALAYA_BAR_DIR{r2} >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \\"$ALAYA_BAR_DIR{r2}\\" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?
"""
# rsynv tomcat
RTOM_TMP = """
sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya/$ALAYA_DIR_TOMCAT{r1} alaya@$IP_ADDRESS:$ALAYA_DIR_TOMCAT{r2} >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" \\"$ALAYA_DIR_TOMCAT{r2}\\" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?
"""


def make_bk_shell():
    with open('www_list.txt', 'rt', newline='') as f:
        with open('www_list.sh', 'a') as s:
            s.write(HEADER)
            s.write(BKHEAD)
            for line in f:
                if line.startswith('/'):
                    p1 = line.strip()
                    if p1.endswith('/'):
                        p2 = p1.rstrip('/')
                    if p1.endswith('*'):
                        p2 = p1
                    shell = BCMD_TMP.format(p1=p1, p2=p2)
                    s.write(shell)
            s.write(BKFOOT)
    print('WWW file list commands finished!')


# rsync shell
def make_rsync_alaya_shell():
    with open('www_rsync_list.txt', 'rt', newline='') as f:
        with open('www_rsync_list.sh', 'a') as s:
            s.write(HEADER)
            s.write(RSHEAD)
            for line in f:
                if line.startswith('/') and '/alaya/' in line:
                    r1 = line.strip()[27:]
                    if r1.endswith('/'):
                        r2 = r1.rstrip('/')
                    if r1.endswith('*'):
                        r2 = r1
                    shell = RALA_TMP.format(r1=r1, r2=r2)
                    s.write(shell)
                if line.startswith('/') and '/tomcat/' in line:
                    r1 = line.strip()[19:]
                    if r1.endswith('/'):
                        r2 = r1.rstrip('/')
                    if r1.endswith('*'):
                        r2 = r1
                    shell = RTOM_TMP.format(r1=r1, r2=r2)
                    s.write(shell)
            s.write(RSFOOT)
    print('WWW file list commands finished!')


if __name__ == '__main__':
    make_bk_shell()
    make_rsync_alaya_shell()