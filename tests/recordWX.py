import wxpy
import pandas as pd
import pymisca.util as pyutil
import json
import functools 

def make__dumpMsg(f=None):
    def dumpMsg(msg, f=f):
        ''' Direct the message to a json dump
    '''
        try:
            dct = msg.raw.copy()
            #### record time to precision
    #         keys = ['create_time','receive_time','latency']
    #         for k in keys:
    #             dct[k] = getattr(msg,k)
            json.dump(dct,f)
            f.write('\n')
        except Exception as e:
            print ('[ERROR]',e)
    #     print (dct)
        print (msg)
    #     json.dump
    return dumpMsg


if __name__ == '__main__':
    bot = wxpy.Bot()
    logDir = '%s-%s'%(bot.self.uin, bot.self.name,)
    pyutil.shellexec(u'mkdir -p {logDir}'.format(**locals()))
    logFile = '%s/messages.json' % logDir
    f =  open(logFile,'a', 0 )
    
    callback  =  make__dumpMsg(f=f)
    chats = bot.friends(update=True) + bot.groups(update=True)    
    bot.register( 
        except_self=False, 
        chats=chats 
    )(callback)
    if not pyutil.hasIPD:
        wxpy.embed()