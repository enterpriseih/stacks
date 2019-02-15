import axios from 'axios'
import qs from 'qs'

const ENV = 'stg'

const BASE_URL = {
  'dev': 'http://localhost:3000/',
  'stg': 'https://localhost/',
  'pro': 'https://localhost/',
}

const HTTP = axios.create({
  baseURL: BASE_URL[ENV],
  headers: {
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
  },
  timeout: 200000,
  transformRequest: [function(data, headers) {
    data = JSON.stringify(data)
    return data
  }],
})

HTTP.interceptors.response.use(function(res) {
  return res
}, function(err) {
  //响应拦截器
  console.log('Error', err.message);
  return Promise.reject(err)
})

const $httpGet = function(url, param = {}) {
  return HTTP.get(qs.stringify(param) === '' ? url : url + '?' + qs.stringify(
      param))
    .then(
      res => res.data
    )
}

const $httpPost = function(url, data) {
  return HTTP.post(url, data).then(
    res => res.data
  )
}

const $httpDel = function(url, param = {}) {
  return HTTP.delete(qs.stringify(data) === '' ? url : url + '?' + qs.stringify(
    param)).then(
    res => res.data
  )
}

export {
  $httpGet, $httpPost, $httpDel
}
