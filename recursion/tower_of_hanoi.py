def hanoi(n,road_from,mid_road,road_to):
    # print(n,road_from,mid_road,road_to)
    # when n-1 plates are in the final position
    if n==1 :
        print("Plate %s from %s to %s"%(n,road_from,road_to))
        return
    # moving n-1 plates off the largest one to be able to move that
    hanoi(n-1,road_from,road_to,mid_road)
    # moving the actual largest one
    print("Plate %s from %s to %s"%(n,road_from,road_to))
    # placing n-1 plates on the top of the largest one
    hanoi(n-1,mid_road,road_from,road_to)


if __name__ == "__main__":
    hanoi(3,'A','B','C')