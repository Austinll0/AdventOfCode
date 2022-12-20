for i in range(1,19):
    if i < 10:
        num = "0" + str(i);
    else:
        num = str(i);
    file = "day" + num + "/day" + str(i) + ".py";
    print("day",i);
    exec(open(file).read())
