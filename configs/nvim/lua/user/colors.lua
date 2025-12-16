-- lua/user/colors.lua

-- Устанавливаем цветовую схему
vim.cmd("colorscheme challenger_deep")

-- Прозрачный фон
vim.cmd([[
  highlight Normal guibg=NONE ctermbg=NONE
  highlight NormalNC guibg=NONE ctermbg=NONE
  highlight NvimTreeNormal guibg=NONE ctermbg=NONE
]])
