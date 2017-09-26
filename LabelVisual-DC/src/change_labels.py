import os 
import sys 

def split_and_move(srcimgdir, srcxmldir, dstimgdir, dstxmldir): 
    import random 
    import shutil

    imgList = os.listdir(srcimgdir)
    xmlList = os.listdir(srcxmldir)
    assert len(imgList) == len(xmlList)

    imgListTrain = random.sample(imgList, 13000)
    imgListTesta = random.sample([img for img in imgList if img not in imgListTrain], 300)
    # imgListValid = []

    count = [0,0,0]
    for img in imgList: 
        imgPath = os.path.join(srcimgdir, img)
        xmlPath = os.path.join(srcxmldir, img[:-4]+'.xml')
        flag = os.path.exists(imgPath) and os.path.exists(xmlPath)

        xdstimgdir = ""
        xdstxmldir = ""

        if flag: 
            if img in imgListTrain: 
                xdstimgdir = os.path.join(dstimgdir,'train', 'images') 
                xdstxmldir = os.path.join(dstxmldir,'train', 'xmls') 
                count[1] += 1
            
            if img in imgListTesta: 
                xdstimgdir = os.path.join(dstimgdir,'test', 'images') 
                xdstxmldir = os.path.join(dstxmldir,'test', 'xmls') 
                count[2] += 1
            
            # if img in imgListValid: 
            #     pass 
            
            if img not in imgListTrain and img not in imgListTesta: 
                count[0] += 1
            
            if xdstimgdir and xdstxmldir:
                if not os.path.exists(xdstimgdir): os.makedirs(xdstimgdir)
                if not os.path.exists(xdstxmldir): os.makedirs(xdstxmldir)
                # shutil.copy(imgname, xdstimgdir)
                # shutil.copy(xmlname, xdstxmldir)
                # shutil.move(imgPath, xdstimgdir)
                # shutil.move(xmlPath, xdstxmldir)
                pass 
            print(count)
        else:
            print("Invalid xmlname: %s")%xmlPath
            # raise Exception("Error")

if __name__ == '__main__': 
    srcimgdir = r'D:\Users\Administrator\Desktop\HGR\hand_dataset\3hand_bk_20170818_labelled\pure\imgs\1'
    srcxmldir = r'D:\Users\Administrator\Desktop\HGR\hand_dataset\3hand_bk_20170818_labelled\pure\xmls\1'
    dstimgdir = r'D:\Users\Administrator\Desktop\HGR\hand_dataset\3hand_bk_20170818_labelled\jiandao_shitou_bu'
    dstxmldir = r'D:\Users\Administrator\Desktop\HGR\hand_dataset\3hand_bk_20170818_labelled\jiandao_shitou_bu'

    split_and_move(srcimgdir, srcxmldir, dstimgdir, dstxmldir)