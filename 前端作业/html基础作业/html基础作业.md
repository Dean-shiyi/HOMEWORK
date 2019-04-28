## 课后练习

1. 使用html列表完成下面图片
![](../../pics/html/html_basic/2.png)
<img src='2.png'>

1. 使用html完成下面图片
![](../../pics/html/html_basic/3.png)
<img src='3.png'>

 
 <a href='html_basic的副本.html'>1.2题答案</a>
 
2. 完成下面的要求
![](../../pics/html/html_basic/1.png)
<img src='1.png'>

 <a href='index.html'>答案</a>
4. 简答什么是html语义化
 
 ```
 在HTML中大多数标签都有其自身的语义，在写代码中应该尽量使用这样的标签，以便于在大量的代码中能识别语句块和其属性归属。而且这样对于搜索引擎优化也是非常有用的
 ```

5. html标签和元素的区别

 ```
 "HTML 标签" 和 "HTML 元素" 通常都是描述同样的意思.但是严格来讲, 一个 HTML 元素包含了开始标签与结束标签
 ```

6. 简答浏览器获取网页的完整大体流程
 
 ```
 一般可分为7个步骤：
1.在浏览器中输入网址；
2.发送至DNS服务器并获得域名对应的WEB服务器的IP地址；
3.与WEB服务器建立TCP连接；
4.浏览器向WEB服务器的IP地址发送相应的HTTP请求；
5.WEB服务器响应请求并返回指定的URL的数据，或错误信息，如果设定重定向，则重定向到新的URL地址。
6.浏览器下载数据后解析HTML源文件，解析的过程中实现对页面的排版，解析完成后在浏览器中显示基础页面。
7.分析页面中的超链接并显示在当前页面，重复以上过程直至无超链接需要发送，完成全部显示。

 ```

7. html css js的区别和功能是什么？
 
 ```
 html： 负责创建，负责语义的表达，解决了页面“显示内容是什么”的问题
 css：负责解决网页中内容该如何显示的问题
 javascript：负责讲解网页内容对事件该做出什么样的反应
 ```

8. 标记语言是什么意思?请再写出两种编辑语言并说明他们的用途
 
 ```
 标记语言，是一种将文本以及文本相关的其他信息结合起来，展现出关于文档结构和数据处理细节的电脑文字编码。与文本相关的其他信息（包括文本的结构和表示信息等）与原来的文本结合在一起，但是使用标记进行标识。标记语言由一系列标签组成，通过标记标签来描述网页。

 编辑语言：HTML   XML
 Xml: XML是元标识语言，用户可以根据自身的需要定义一些标记 
 Html: 这是一种用来制作超文本文档的简单标记语言，用其编写的文档通常后缀为html
 
 ```

9. h5播放器和 flash播放器的有什么不同点
 
 ```
1.Flash：YouTube上的FLV影片得通过一个SWF（Shockwave Flash）播放器播放，而这个播放器会呼叫Flash Player Plug-In来播放影片。
2.HTML5：YouTube上的M4V影片直接利用标签即可播放，而播放器是以JavaScript写成，一切都以浏览器内建功能完成.
 ```
10. 如何区分 HTML 和 HTML5
 
 ```
 1、在文档类型声明上
 HTML声明：<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/
 DTD/xhtml1-transitional.dtd">
 <html xmlns="http://www.w3.org/1999/xhtml">
 HTML5声明：<!doctype html>
 上面的两种声明,HTML5声明简洁方便人们的记忆，HTML声明太长了并且很难记住这段代码。

 2、在结构语义上
 HTML:没有体现结构语义化的标签，通常都是这样来命名的<div id="header"></div>，这样表示网站的头部。
 HTML5:在语义上却有很大的优势，提供了一些新的HTML5标签比如: article、footer、header、nav、section，这些通俗易懂。 
　　
 ```