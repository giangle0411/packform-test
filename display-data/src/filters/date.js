export default value => {
  const defaultDate = new Date(value)

  const options = {
    timeZone: 'Australia/Melbourne',
    day: '2-digit',
    month: 'short',
    hour: '2-digit',
    minute: '2-digit'
  }
  const date = defaultDate.toLocaleString(['en-UK'], options).split(', ')
  const dateSplited = date[0].split(' ')
  const month = dateSplited[0]
  const day = dateSplited[1]
  const time = date[1]
  return month + ' ' + getOrdinalNum(day) + ', ' + time
}

const getOrdinalNum = number => {
  let selector

  if (number <= 0) {
    selector = 4
  } else if ((number > 3 && number < 21) || number % 10 > 3) {
    selector = 0
  } else {
    selector = number % 10
  }

  return number + ['th', 'st', 'nd', 'rd', ''][selector]
}
