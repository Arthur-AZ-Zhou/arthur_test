def spaceship_building(cans):
    total_cans =0
    for week in range(0,53):
            total_cans = total_cans + cans
            print('Week %s = %s cans' % (week, total_cans))


spaceship_building(10)

print(time.asctime())


