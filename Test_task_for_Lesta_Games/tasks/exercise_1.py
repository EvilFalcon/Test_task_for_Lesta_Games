# Реализация 1 (базовая):
def isEven1(value):
  return value % 2 == 0


#Реализация 2 (битовая проверка):
def isEven2(value):
  return (value & 1) == 0