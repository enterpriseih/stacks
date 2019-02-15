import {
  $httpGet, $httpPost, $httpDel
}
from '../util.js'

export function getUser() {
  return $httpGet('/user')
}

export function createUser(data) {
  return $httpPost('/user', data)
}

export function deleteUser(user_id) {
  return $httpDel('/user', {
    id: user_id
  })
}
