namespace DemoGame.domain.units
{
    public class Tumbleweed : IUnit
    {
        public int Id => 5;
        public string Name => "Tumbleweed";
        public int HitPoints => 30;
        public int Attack => 0;
        public int Defence => 60;
        public int Cost => 60;
        public bool Cloneable => false;
        public bool Curable => false;

        public double SpecialActionProbability => 0.5;
        public void SpecialAction(Army friends, Army enemies)
        {
            throw new System.NotImplementedException();
        }
    }
}