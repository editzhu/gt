import json
with open("f:/utry (739).json",'r') as load_f:
  load_dict = json.load(load_f)
  #json_str = json.dumps(load_dict)
  shapes=load_dict["shapes"]
  print(shapes)
  print(type(shapes))
  print("--------------")
  maxarea=0
  x1=0
  y1=0
  x2=0
  y2=0
  for i in shapes:
    label=i["label"]
    points=i["points"]

    if label != "道路" and label != "人" and label != "汽车":
        print ("序号：%s   值：%s" % (shapes.index(i) + 1, label))
        print (points)
        maxx=0
        maxy=0
        minx=10000
        miny=10000
        for i in points:
          print ("    序号：%s   值：%s" % (points.index(i) + 1, i))
          if i[0]>maxx: maxx=i[0]
          if i[0]<minx: minx=i[0]
          if i[1]>maxy: maxy=i[1]
          if i[1]<miny: miny=i[1]
        maxx=int(maxx)
        minx=int(minx)
        maxy=int(maxy)
        miny=int(miny)
        area = (maxx-minx)*(maxy-miny)
        if area>maxarea :
          maxarea = area
          x1 = minx
          y1 = miny
          x2 = maxx
          y2 = maxy
        print ("本区域外接最小矩形-面积-----------",maxx,maxy,minx,miny,area)  
print("本图最大区域-面积--------",x1,y1,x2,y2,maxarea) 

  
  

