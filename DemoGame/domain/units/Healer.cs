namespace DemoGame.domain.units
{
	public class Healer : IUnit
	{
		public int Id => 1;
		public string Name => "Healer";
		public int HitPoints => 20;
		public int Attack => 10;
		public int Defence => 10;
		public int Cost => 30;
		public bool Cloneable => false;
		public bool Curable => true;

		public double SpecialActionProbability => 0.5;
		public void SpecialAction(Army friends, Army enemies)
		{
			throw new System.NotImplementedException();
		}
	}
}