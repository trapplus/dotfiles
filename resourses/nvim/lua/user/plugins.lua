-- lua/user/plugins.lua

-- Путь к lazy.nvim
local lazy_path = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"

-- Если не установлен — клонируем
if not vim.loop.fs_stat(lazy_path) then
  vim.fn.system({
    "git", "clone", "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    lazy_path
  })
end

vim.opt.rtp:prepend(lazy_path)

-- Подключаем плагины
require("lazy").setup({
  -- Плагин для дерева файлов
  { "nvim-tree/nvim-tree.lua", config = true },

  -- Git команды прямо в Neovim
  { "tpope/vim-fugitive" },

  -- Красивый статусбар
  {
    "nvim-lualine/lualine.nvim",
    config = function()
      require("lualine").setup()
    end
  },

  -- Подсказки по биндам
  {
    "folke/which-key.nvim",
    config = function()
      require("which-key").setup()
    end
  },

  -- Цветовая схема challenger deep
  { "challenger-deep-theme/vim", name = "challenger-deep" }
})

