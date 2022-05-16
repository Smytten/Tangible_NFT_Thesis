# World builder documentation

## Tile types
The tile types are as follows

<ul>
  <li>Water Tile</li>
    <ol>
      <li>Deep Water</li>
      <li>Shallow Water</li>
      <li>Normal Water</li>
    </ol>
  <li>Earth Tile</li>
    <ol>
      <li>Dessert Tile</li>
      <li>Forrest Tile</li>
    </ol>
  <li>Mountain Tile</li>
    <ol>
      <li>Snowy Mountain</li>
      <li>Rock Mointain</li>
    </ol>
  </li>
   <li>Valley Tile</li>
    <ol>
      <li>Deep Valley</li>
      <li>Shallow Valley</li>
    </ol>
  </li>
</ul>

The tile type is the only thing needed to be supplied, The logic of implemning the visual is handel on board. 

## World 
The world consist of Flowers and Binders. Flowers are the acutated point and consist of a pentagon in the middle and 5 hexigons on the side. Binders are the panel which binds the different Flowers together. 

On the world there is 6 flowers, the location is addressed based on a rule. Always start from the center. Then go clockwise out. Thus the on the center location 0, then 1 on the top right and so on. 

## Flower
A Flower consist of 6 panels. 5 panels of which a hexagons and a singe pentagon. The location of the panels follows the same logic. The center panel, the pentagon, location is 0, then the top right is 1 and so on. 



## Binder


# Height

Max height 90, min height -90