(set-background-color "black")
(set-foreground-color "white")
(set-cursor-color     "white")

(setq compilation-window-height 12)
(require 'compile)
(add-hook 'c++-mode-hook
          (lambda ()
            (set (make-local-variable 'compile-command)
                 (format "SOURCE=%s;myg++" file))))

(custom-set-variables
 '(global-font-lock-mode t nil (font-lock))
 '(mouse-wheel-mode t nil (mwheel))
 '(column-number-mode t)
 '(indent-tabs-mode nil)
 '(inhibit-splash-screen t)
 '(inhibit-startup-screen t)
 '(scroll-bar-mode (quote right))
 '(show-paren-mode t nil (paren))
 '(tool-bar-mode nil nil (tool-bar))
 '(transient-mark-mode t))
