##########################################
##					##
##		文件说明		##
##					##
##########################################
CHINESE-OCR/ 		源代码
ctpn_data/		样本集
docker/			dockerfile文件和相关脚本
testFlaskjosn.js	测试Flask服务开启后，客户端的json接收例子



##########################################
##					##
##		训练流程		##
##					##
##########################################



1. push代码到master分支，创建git新分支idcar_branch
2. ctpn数据集制作

3. 在新分支上修改代码
1）/home/leo/PythonProjects/CHINESE-OCR/CHINESE-OCR_workspace/CHINESE-OCR/ctpn/lib/datasets/pascal_voc.py
 （1）取消下面几行代码注释
	# cls_objs = [
        #     obj for obj in objs if obj.find('name').text in self._classes
        # ]
        # objs = cls_objs
 （2）修改如下训练数据集路径
	self._devkit_path = '/Users/xiaofeng/Code/Github/dataset/CHINESE_OCR/ctpn/VOCdevkit2007'
      为
	self._devkit_path = '../../../../../ctpn_data/VOCdevkit2007'
2） /home/leo/PythonProjects/CHINESE-OCR/CHINESE-OCR_workspace/CHINESE-OCR/ctpn/ctpn/text.yml
	是否更改 “NCLASSES: 2” 后面分类数2

4. 训练
	/home/leo/PythonProjects/CHINESE-OCR/CHINESE-OCR_workspace/CHINESE-OCR/ctpn/ctpn/train_net.py
	1） 修改如下路径
		pretrained_model=
		'/Users/xiaofeng/Code/Github/dataset/CHINESE_OCR/ctpn/pretrain/VGG_imagenet.npy',
	    为
		pretrained_model=
		'/Users/xiaofeng/Code/Github/dataset/CHINESE_OCR/ctpn/pretrain/VGG_imagenet.npy',

需要配置路径位置：

/home/leo/PythonProjects/CHINESE-OCR/CHINESE-OCR_workspace/CHINESE-OCR/angle/predict.py
/home/leo/PythonProjects/CHINESE-OCR/CHINESE-OCR_workspace/CHINESE-OCR/ctpn/ctpn/model.py
/home/leo/PythonProjects/CHINESE-OCR/CHINESE-OCR_workspace/CHINESE-OCR/ctpn/ctpn/other.py
/home/leo/PythonProjects/CHINESE-OCR/CHINESE-OCR_workspace/CHINESE-OCR/ctpn/lib/fast_rcnn/config.py
/home/leo/PythonProjects/CHINESE-OCR/CHINESE-OCR_workspace/CHINESE-OCR/ocr/model.py
/home/leo/PythonProjects/CHINESE-OCR/CHINESE-OCR_workspace/CHINESE-OCR/train/pytorch-train/crnn_main.py
/home/leo/PythonProjects/CHINESE-OCR/CHINESE-OCR_workspace/CHINESE-OCR/ctpn/lib/datasets/pascal_voc.py
/home/leo/PythonProjects/CHINESE-OCR/CHINESE-OCR_workspace/CHINESE-OCR/ctpn/ctpn/train_net.py









