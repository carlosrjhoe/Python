def mostarPicnic(itemsDict, leftWidth, rightWidth):
    print(" PICNIC ITEMS ".center(leftWidth + rightWidth,"="))
    for i, j in itemsDict.items():
        print(f"{i.ljust(rightWidth)} {str(j).rjust(rightWidth)}")

if __name__ == "__main__":
    picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
    mostarPicnic(picnicItems, 15, 15)
    mostarPicnic(picnicItems, 15, 15)