namespace DemoGame.domain.units.armor
{
    public interface IArmor
    {
        string Name { get; set; }
        int Defence { get; set; }
        int Attack { get; set; }
        float Durability { get; set; } // Надёжность: с какой вероятностью сломается
    }
}