# npm

## cnpm

```bash
npm install -g cnpm --registry=<https://registry.npm.taobao.org>
```

## basic

```bash
# init unscoped modules
npm init

# init scoped modules
npm init --scope=@scope-name

# install custom repository
npm install git+ssh://git@<domain>:<group_or_username>/<project#branch> -S

# update module
npm update <module>

# publish unscoped modules or scoped private module
npm publish
# publish scoped publid
npm publish --access public
# after publishing, open https://www.npmjs.com/package/[new-package-name]/

# update existing readme
npm version patch
npm publish

# create tarball
npm pack <package>
```
