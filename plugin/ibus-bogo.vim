if !has('python')
    finish
endif

let s:path = fnamemodify(resolve(expand('<sfile>:p')), ':h')
let s:pyscript = s:path . '/toggle.py'

" xkb:us::eng or bogo
function! SetIbusEngine(name)
    execute 'pyfile ' . s:pyscript
endfunc

autocmd! InsertLeave * call SetIbusEngine('xkb:us::eng')
autocmd! InsertEnter * call SetIbusEngine('bogo')
