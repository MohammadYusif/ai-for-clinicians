-- Level-1 headings are the topic slides of a deck. Give each one the dark ground that the
-- title slide has, so a deck reads as: dark topic slide, then white working slides.
function Header(el)
  if el.level == 1 then
    el.classes:insert("dark")
    if el.attributes["data-background-gradient"] == nil and el.attributes["data-background-color"] == nil then
      el.attributes["data-background-gradient"] = "linear-gradient(135deg, #0f172a 0%, #1e1b4b 55%, #0f766e 135%)"
    end
  end
  return el
end
