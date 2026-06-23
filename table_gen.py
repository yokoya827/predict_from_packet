import datetime

pupulation = [[]*4]*13


def table_cooking(population):

    dt_now = datetime.datetime.now()
    '''
    cell1 = ''
    cell2 = ''
    cell3 = ''
    cell4 = ''
    cell5 = ''
    cell6 = ''
    cell7 = ''
    cell8 = ''
    cell9 = ''
    cell10 = ''
    cell11 = ''
    cell12 = '' 
    cell13 = ''
    part1 = '<table class="termux_table"><tr style="text-align: center;"><td>場所</td><td>現在時刻</td><td>10分後</td><td>30分後</td><td>1時間後</td></tr><tr style="text-align: center;">'
    #part2 = '<table class="termux_table"><tr style="text-align: center;"><td>1月</td><td>2月</td></tr><tr style="text-align: center;">'
    #<td>3月</td><td>4月</td><td>5月</td><td>6月</td><td>7月</td><td>8月</td><td>9月</td><td>10月</td><td>11月</td><td>12月</td></tr><tr style="text-align: center;">'
    
    for x in population[0]:
        cell1 += '<td>' + str(x) + '</td>'
    for x in population[1]:
        cell2 += '<td>' + str(x) + '</td>'
    for x in population[2]:
        cell3 += '<td>' + str(x) + '</td>'
    for x in population[3]:
        cell4 += '<td>' + str(x) + '</td>'
    for x in population[4]:
        cell5 += '<td>' + str(x) + '</td>'
    for x in population[5]:
        cell6 += '<td>' + str(x) + '</td>'
    for x in population[6]:
        cell7 += '<td>' + str(x) + '</td>'
    for x in population[7]:
        cell8 += '<td>' + str(x) + '</td>'
    for x in population[8]:
        cell9 += '<td>' + str(x) + '</td>'
    for x in population[9]:
        cell10 += '<td>' + str(x) + '</td>'
    for x in population[10]:
        cell11 += '<td>' + str(x) + '</td>'
    for x in population[11]:
        cell12 += '<td>' + str(x) + '</td>'
    for x in population[12]:
        cell13 += '<td>' + str(x) + '</td>'
    
   

    product = part1 + cell1 + '</tr>' + cell2  + '</tr>' +cell3 + '</tr>' + cell4 + '</tr>' + cell5 + '</tr>' + cell6 + '</tr>' + cell7  + '</tr>' + cell8 + '</tr>' + cell9 + '</tr>' + cell10 + '</tr>' + cell11 + '</tr>' + cell12 + '</tr>'+ cell13 + '</tr></table>'
  
    '''
    product = '現在時刻は\t' + str(dt_now.hour) + ':' + str(dt_now.minute) + '</tr>'

    return product


if __name__ == '__main__':
    print(table_cooking(pupulation))