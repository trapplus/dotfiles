-- Подключаем все модули, которые находятся в папке lua/user/
require("user.options")   -- Базовые настройки
require("user.keymaps")   -- Кастомные бинды
require("user.plugins")   -- Плагины через Lazy
require("user.colors")    -- Цветовая схема и прозрачность


local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable",
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)
