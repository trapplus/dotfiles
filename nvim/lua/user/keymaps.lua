-- lua/user/keymaps.lua

-- Устанавливаем клавишу <leader> на пробел
vim.g.mapleader = " "

-- Быстрое присвоение биндов
local keymap = vim.keymap.set

-- Основные команды
keymap("n", "<leader>w", ":w<CR>", { desc = "Сохранить файл" })
keymap("n", "<leader>q", ":q<CR>", { desc = "Выйти" })

-- Открыть файловый менеджер
keymap("n", "<leader>e", ":NvimTreeToggle<CR>", { desc = "Открыть дерево файлов" })

-- Git статус
keymap("n", "<leader>gs", ":G<CR>", { desc = "Git status" })

