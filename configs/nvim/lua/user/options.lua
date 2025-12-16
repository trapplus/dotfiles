-- lua/user/options.lua

-- Относительная нумерация строк
vim.opt.number = true
vim.opt.relativenumber = true

-- Цвета и интерфейс
vim.opt.termguicolors = true -- 24-битные цвета
vim.opt.background = "dark"  -- Цветовая схема в тёмном режиме
vim.opt.cursorline = true    -- Подсвечивать текущую строку

-- Автоотступ и табуляция
vim.opt.smartindent = true -- Умный отступ
vim.opt.autoindent = true  -- Повторяет отступ предыдущей строки
vim.opt.expandtab = true   -- Таб = пробел
vim.opt.tabstop = 4        -- Ширина таба
vim.opt.shiftwidth = 4     -- Отступ при >> и <<

-- Поддержка мыши
vim.opt.mouse = "a" -- Включить мышку везде

-- Буфер обмена
--vim.opt.clipboard = "unnamedplus" -- Использовать системный буфер

-- Чистота интерфейса
vim.opt.fillchars:append({ eob = " " }) -- Убирает тильды (~) в конце
