def main():
  f = open('nums.txt', 'rU')

  s = 0
  limit = 10**39
  for line in f:
    n = int(line)/limit
    s += n

  print ('\nThe reuslt is ...', (s/( 10 **(len(str(s)) - 10)))*10000)

if __name__ == '__main__':main()