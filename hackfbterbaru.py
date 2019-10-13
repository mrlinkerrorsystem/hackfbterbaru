#decompiled by MRLINKERRORSYSTEM
import os, sys
print '\x1b[1;32mSudah punya ID dan Password nya?'
print '\x1b[1;32mSilahkan Login '
import os, sys

def wa():
    os.system('xdg-open https://api.whatsapp.com/send?phone=628149281196&text=Assalamualaikum')


def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


user = raw_input('ID: ')
import getpass
sandi = raw_input('Password: ')
if sandi == 'Cyber' and user == 'Mrlink':
    print 'Anda Telah Login'
    sys.exit
else:
    print 'Login GAGAL, Silahkan hubungi ADMIN untuk Beli Toolsnya'
    wa()
    restart()
